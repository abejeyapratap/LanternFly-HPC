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

The Conda Environment for TensorFlow CPU is now ready to use.

### Submitting a Slurm Job on Picotte
- Copy the batch job scripts (cpu-mnist.sh / gpu-mnist.sh) and classification script (hpc.py) to your mnist directory on Picotte.

- cpu-mnist.sh is a script meant to run a single-multithreaded program that *can* utilize multiple CPU cores.
- To submit a slurm job request on Picotte for CPU-only:

```bash
sbatch cpu-mnist.sh
```
- gpu-mnist.sh is a script that utilizes a single NVIDIA GPU device & CUDA through TensorFlow on Picotte.
- To submit a slurm job request on Picotte for GPU and CPU:

```bash
sbatch gpu-mnist.sh
```

### Output
- The output of the job should contain 3 files:
  
  - slurm-XXXX.out
  - verification.png
  - recognition_model.hdf5
- The PNG file is the matplot-saved image of the model.
- The output file contains training information about the running script.
- The HDF5 file contains the actual trained model ready for use by exporting.

### Optimizations & Performance
Regardless of the submitted job script, the job should take under 25 seconds, on average.

The primary goal of using High-Performance Computing is to reduce the training times through big data processing. However, this does not happen automatically. Infact, when I first ran the classification script on Picotte, it took *1150.549 seconds* to train on CPU-only despite using the maximum available compute resources. This has to do with multi-threading and distribution of workload among cores.

Through a series of experiments and trial runs, I've almost fully optimized both batch scripts. For comparison, the classification model takes *60 seconds* to train locally on my MacBook Pro. 

Here are the results on Picotte:
- CPU-only: the classification model takes **23.0460** seconds to train
- GPU+CPU: the classification model takes **13.4592** seconds to train

### Final Scripts
- hpc.py
  - TensorFlow MNIST image classification Python script
- cpu-mnist.sh
  - Slurm batch job script optimized to run on Picotte's def partition
- gpu-mnist.sh
  - Slurm batch job script optimized to run on Picotte's gpu partition