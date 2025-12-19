# %%
import os
import tempfile
import multiprocessing
from multiprocessing import cpu_count

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import scvi
import seaborn as sns
from scvi.external import MRVI

scvi.settings.seed = 0  # optional: ensures reproducibility
print("Last run with scvi-tools version:", scvi.__version__)
save_dir = tempfile.TemporaryDirectory()

# 1) Restart the Python kernel before running this cell.
# 2) Set spawn start method BEFORE any CUDA interaction.
multiprocessing.set_start_method("spawn", force=True)

# %%
adata_path = "sound_life_t_cd4_memory.h5ad"
adata = sc.read(adata_path)

adata

# %%
sample_key = "subject.subjectGuid"  # target covariate for MrVI
batch_key = "batch_id"  # batch covariate for MrVI

MRVI.setup_anndata(adata, sample_key=sample_key, batch_key=batch_key, backend="torch")

# %%
model = MRVI(adata, backend="torch")

# batch_size passed to model.train (adjust to GPU memory)
batch_size = 512 * 16

# start training
model.train(
    max_epochs=100,
    batch_size=batch_size,
    accelerator="gpu",
    devices=1,
    # datasplitter_kwargs={"num_workers": 24}
)

# %%
# Save the model
model.save("mrvi_model_cd4_memory", save_anndata=True, overwrite=True)

# %%
plt.plot(model.history["elbo_train"])

# %%
u = model.get_latent_representation(batch_size=batch_size)

# %%
z = model.get_latent_representation(batch_size=batch_size, give_z=True)

# %%
adata.obsm["u"] = u
adata.obsm["z"] = z

# %%
# Save the new adata with u and z embeddings
adata.write("sound_life_t_cd4_memory_with_embeddings.h5ad")


# %%
sc.pp.neighbors(adata, use_rep="u")
sc.tl.umap(adata, min_dist=0.3)

# %%
fig, ax = plt.subplots(figsize=(6, 6), dpi=300)

sc.pl.umap(
    adata,
    # color=["initial_clustering", "Status"],
    color=[batch_key, sample_key],
    frameon=False,
    ncols=1,
    ax=ax,
    figure=fig,
    show=False,
)

# %%
sc.pp.neighbors(adata, use_rep="z")
sc.tl.umap(adata, min_dist=0.3)

# %%
fig, ax = plt.subplots(figsize=(6, 6), dpi=300)

sc.pl.umap(
    adata,
    # color=["initial_clustering", "Status"],
    color=[batch_key, sample_key],
    frameon=False,
    ncols=1,
    ax=ax,
    figure=fig,
    show=False,
)


