#! /bin/bash 
#SBATCH --nodes=1
#SBATCH --mem=1G
#SBATCH --ntasks-per-node=2
#SBATCH --time=00:03:00
#SBATCH --partition=devel
#SBATCH --job-name=sl_test

#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=felix.krones@oii.ox.ac.uk

module load Anaconda3
source activate /data/inet-multimodal-ai/wolf6245/envs/example_env
conda info --env

my_argument="My_new_argument"

python main.py --argument $my_argument
