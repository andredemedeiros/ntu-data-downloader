#!/bin/bash

## SLURM CONFIGURATIONS

#SBATCH --partition=prod10
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=8G                   
#SBATCH --time=24:0:0            
#SBATCH --job-name=ntu_xtr
#SBATCH --output=log_download_%j.txt

## ENVIRONMENT AND EXECUTION

source ./venv/bin/activate
python extract_zips.py