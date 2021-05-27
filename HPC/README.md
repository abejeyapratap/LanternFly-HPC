# High-Performance Computing & GPU Processing

###### Abe Jeyapratap

## Connecting to Picotte (Drexel URCF's HPC Cluster)
See tutorial found in Documents/Software Team/GPU Processing/Connecting to Picotte - Abe Jeyapratap.pptx

## Picotte Environments

Before running the TensorFlow MNIST Classification model on Picotte, there are some important setup steps to complete:

- Login to Picotte: ssh userName@picottelogin.urcf.drexel.edu
- Switch to Anaconda Python by running the following commands:

	```
    mkdir mnist
    cd mnist
    module load python/anaconda3
	conda init
	```
- Log out

### Creating Conda Environments

Now that Anconda Python is setup, the Conda Environment that runs TensorFlow must be created. I've created all the environment files necessary to replicate a working TensorFlow Conda environment on Picotte.

On the command-line, run the following commands from the GitHub HPC Directory:

```
scp environment.yml userName@picottelogin.urcf.drexel.edu:~/mnist/
```
- Login to Picotte, navigate to the mnist directory, and run the command:

```
conda env create -f environment.yml
```

- You should see a message saying "To activate this environment..." Check if the environment is created and activate it.

```
conda info -e
conda activate tf-mnist2
```

The Conda Environment is now ready to use.

### Submitting a Slurm Job on Picotte
- Copy the batch job script (mnist.sh) and classification script (hpc.py) to your mnist directory on Picotte.

- Submit a slurm job request on Picotte:

```bash
sbatch mnist.sh
```
- The job should take approximately 30 seconds.
- The output of the job contains 2 files:
  
  - slurm-XXXX.out
  - verification.png
- The PNG file is the matplot image of the model.
- The output file contains training information about the running script.