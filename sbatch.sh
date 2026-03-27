#!/bin/bash
#SBATCH --partition=prod10
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=8G                   
#SBATCH --time=24:0:0            
#SBATCH --job-name=ntu_dl
#SBATCH --output=log_download_%j.txt


source ./venv/bin/activate

# Vai para o diretório do projeto
cd ./ntu-data-downloader

# Executa o script Python
python main.py