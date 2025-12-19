#!/bin/bash
#SBATCH --job-name=fit_mrvi
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --time=20:00:00
#SBATCH --mem=200G
#SBATCH --gres=gpu:1
#SBATCH --exclusive
#SBATCH --output=fit_mrvi_%A_%a.out
#SBATCH --error=fit_mrvi_%A_%a.out

source /home/mgiammar/miniconda3/bin/activate /home/mgiammar/miniconda3/envs/scvi-tools

python /shared/mgiammar_tests/cs294_hw/fit_mrvi_sound_of_life.py