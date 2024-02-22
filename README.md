# Hello World Cluster Example

## Overview
This repository contains a simple "Hello World" Python script designed to run on a computing cluster managed with Slurm. The setup demonstrates the basic workflow of environment setup, script execution, and job management on a Slurm-managed cluster.

## Files in the Repository
- `LICENSE`: The license file for the project.
- `README.md`: This file, containing documentation for the repository.
- `main.py`: The main Python script that prints "Hello, World!" and demonstrates basic usage of the NumPy package.
- `build_env.sh`: Script to build the Python environment on the cluster.
- `run_script.sh`: Script to schedule the `main.py` script as a job on the cluster using Slurm.
- `requirements.txt`: List of Python packages required to run `main.py`.
- `main_gpu_test.py`: This is a new file to test the GPUs.

## Setting Up the Environment
1. To set up the Python environment on your cluster, run the `build_env.sh` script. This script installs necessary Python packages as specified in `requirements.txt`.

    sh build_env.sh

2. Ensure that the same environment name is used in both `build_env.sh` and `run_script.sh` for consistency.

## Running the Script
1. To schedule the `main.py` script as a job on the cluster, use the `run_script.sh` script with Slurm's `sbatch` command.

    sbatch run_script.sh

## Managing Jobs
- **Check Queue**: To view your queued jobs, use the command `squeue -u user_name`, replacing `user_name` with your actual cluster username.
- **Cancel Job**: If you need to cancel a job, use the command `scancel job_name`, where `job_name` is the name of the job you wish to cancel.

## License
This project is licensed under the terms of the [LICENSE](LICENSE) file in this repository.
