#!/bin/bash
#SBATCH --mail-user=aj928@drexel.edu
#SBATCH --partition=def
#SBATCH --nodes=1
#SBATCH --ntasks-per-core=1
#SBATCH --cpus-per-task=8
#SBATCH --time=00:30:00
#SBATCH --mem=160G

## Name: Abe Jeyapratap
## Purpose: Run MNIST Classification Model on Picotte with CPU only (non-optimized)
## Date: 5/27/21

# Use Anaconda Python & Initialize Shell with login script
module load python/anaconda3
. ~/.bashrc

# Activate the Conda environment
if [ $SLURM_JOB_PARTITION == "gpu" ]
then
    echo -e "\nRunning on GPU\n"
else
    echo -e "\nRunning on CPU\n"
    conda activate tf-mnist2
    # conda activate tf24
fi

# Run the MNIST Classification script
python3 ./hpc.py