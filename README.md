# NTU RGB+D 120 Data Downloader

This project allows you to automatically download the **NTU RGB+D 120** dataset and related datasets from the [NTU Action Recognition Dataset](https://rose1.ntu.edu.sg/dataset/actionRecognition/), organizing the files into separate folders by section.  

The script supports parallel downloads (up to 3 files at a time) and checks whether a file has already been downloaded to avoid duplication.

## Project structure

```bash
ntu-data-downloader/
├─ main.py                # Main script to start downloads
├─ download_utils.py      # Download and progress functions
├─ credentials.py         # User and password configuration
├─ requirements.txt       # Required Python libraries
├─ downloads/             # Output folder for files (generated automatically)
```

## Setup

```bash
git clone https://github.com/andredemedeiros/ntu-data-downloader
cd ntu-data-downloader

python3 -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## credentials.py
Create a file named credentials.py in the project root directory with the following content:

```bash
USERNAME = "seu_usuario_ntu"
PASSWORD = "sua_senha_ntu"
```
## To Use

```bash
python main.py  
```

# Data
## 2.1 "NTU RGB+D 120" - 3D Skeletons
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/158

## 2.2 "NTU RGB+D 120" - Masked Depth Maps
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/82
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/84 <br>
to (2++) <br>
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/110

## 2.3 "NTU RGB+D 120" - Full Depth Maps
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/42
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/159
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/160 <br>
to (1++) <br>
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/172

## 2.4  "NTU RGB+D 120" - RGB videos
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/142 <br>
to (1++) <br>
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/156

## 2.5 "NTU RGB+D 120" - IR videos
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/105
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/107
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/109
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/113
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/115
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/117
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/119
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/40
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/45
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/43
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/120
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/121
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/122
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/123
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/124

## 3.0 AUTH UAV Gesture Dataset (NTU 4-Class)
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/221

## TVBench
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/230