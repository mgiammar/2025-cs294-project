# CS294 Course Project - Analyzing effect of age on immunization response

TODO: Motivation

## Datasets

Data were pulled from [Gong, Q., Sharma, M., Glass, M.C. et al. Multi-omic profiling reveals age-related immune dynamics in healthy adults. Nature (2025).](https://doi.org/10.1038/s41586-025-09686-5), specifically the pre-normalized, pre-transformed sequencing data for the CD4 memory T-cells were downloaded from the [Allen Institute](https://apps.allenimmunology.org/aifi/insights/dynamics-imm-health-age/downloads/scrna/).
This subset constitutes 2.6 million which were used because of computational constraints (rather than the full 13 million cells).

- `sound_life_t_cd4_memory.h5ad`: Downloaded single-cell sequencing file.
- `sound_life_t_cd4_memory_with_embeddings.h5ad`: Same dataset, except model embeddings in the _u_ and _v_ spaces are included.

## Analyses and scripts

- `fit_mrvi_sound_of_life.ipynb`: Interactive notebook used to begin MrVI fittings adapted from the MrVI quickstart guide.
- `fit_mrvi_sound_of_life.py`: Python script exported from the above notebook, used for async execution in training.
- `fit_mrvi.sh`: SLURM batch script to run the MrVI fitting.
- `analyze_mrvi_model.ipynb`: Notebook that goes through for the analysis of the fitted MrVI model.


## Other files

- `mrvi_model_cd4_memory/`: Directory containing fitted MrVI 