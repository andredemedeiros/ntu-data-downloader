# NTU RGB+D 120 Dataset Downloader

This project allows you to automatically download the complete **NTU RGB+D 120** dataset from the [NTU Action Recognition Dataset](https://rose1.ntu.edu.sg/dataset/actionRecognition/), organizing the files into separate folders by section.  

The script supports **parallel downloads** (up to 5 files at a time) and checks whether a file has already been downloaded to avoid duplication. Additionally, you can verify if downloaded files are **complete and not corrupted** using the verification script.

## Project structure

```bash
ntu-data-downloader/
├─ main.py                # Main script to start downloads
├─ download_utils.py      # Download and progress functions
├─ credentials.py         # User and password configuration
├─ verify_downloads.py    # Verify completeness and integrity of downloaded files
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
USERNAME = "your_ntu_user"
PASSWORD = "your_ntu_password"
```
## Download
To downlod the complete dataset:

```bash
python main.py  
```

## Verify download
After downloading, you can check which files are complete or incomplete/corrupted:

```bash
python verify_downloads.py
```

## License and Disclaimer
This project is licensed under the MIT License - see the LICENSE file for details.
This project only provides tools to download the dataset.

The NTU RGB+D 120 dataset is not distributed with this repository.
Users must comply with the official dataset license and terms of use.

## Citation
Jun Liu, Amir Shahroudy, Mauricio Perez, Gang Wang, Ling-Yu Duan, Alex C. Kot, "NTU RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Understanding", IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2019.
<br>
F. Patrona, I. Mademlis, I. Pitas, “An Overview of Hand Gesture Languages for Autonomous UAV Handling”, in Proceedings of the Workshop on Aerial Robotic Systems Physically Interacting with the Environment (AIRPHARO), 2021.



<!-- # Dataset
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
https://rose1.ntu.edu.sg/dataset/actionRecognition/download/230 -->

