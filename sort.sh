#!/bin/bash

#SBATCH --partition=gpu
#SBATCH --job-name=spike_sort
#SBATCH --gpus=1
#SBATCH --time=24:00:0
#SBATCH --ntasks 1
#SBATCH --mem=100G
#SBATCH --nodes=1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=skylerthomas@umass.edu
#SBATCH --error=/work/current_projects/spike_sort/logs/%x_%j.err
#SBATCH --output=/work/current_projects/spike_sort/logs/%x_%j.out 


export LOAD=/work/pi_moorman_umass_edu/ephys_chris/CPWI15_2019_06_19_14_17_39_LRRL_220uA
export WORK=/work/skylerthomas_umass_edu/current_projects/spike_sort
export SAVE=/work/skylerthomas_umass_edu/current_projects/graphs

cd $WORK 

module purge
module load conda
conda activate spike_sort

python $WORK/sort.py
