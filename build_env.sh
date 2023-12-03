#! /bin/bash

# Load the version of Anaconda you need
module load Anaconda3

# Create an environment in $DATA and give it an appropriate name
export CONPREFIX=$DATA/envs/your_env_name
conda create --prefix $CONPREFIX python=3.11

# Activate your environment
source activate $CONPREFIX

# Install packages...
conda install --file requirements.txt
