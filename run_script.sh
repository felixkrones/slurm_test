#! /bin/bash 
#SBATCH --nodes=1
#SBATCH --mem=120G
#SBATCH --ntasks-per-node=28
#SBATCH --time=00:10:00
#SBATCH --partition=devel
#SBATCH --job-name=sl_test

#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=felix.krones@oii.ox.ac.uk

module load Anaconda3
source activate /data/inet-multimodal-ai/wolf6245/envs/example_env
conda info --env

my_argument="My new argument"

python -m main.py --argument $my_argument
