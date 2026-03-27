# download_utils.py
import requests
from bs4 import BeautifulSoup
import os
from rich.progress import Progress, BarColumn, DownloadColumn, TextColumn, TimeRemainingColumn
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://rose1.ntu.edu.sg/dataset/actionRecognition/download/"
LOGIN_PAGE = "https://rose1.ntu.edu.sg/login/"

def start_session(username, password):
    """Log in and return the requests.Session() object"""
    session = requests.Session()
    response = session.get(LOGIN_PAGE)
    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]

    payload = {
        "username": username,
        "password": password,
        "csrfmiddlewaretoken": csrf_token
    }

    headers = {
        "Referer": LOGIN_PAGE,
        "User-Agent": "Mozilla/5.0"
    }

    session.post(LOGIN_PAGE, data=payload, headers=headers)
    print("Logged in")
    return session

def download_file(session, url, folder, progress, task_id):
    """Download file with Rich progress bar"""
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, url.split("/")[-1] + ".zip")

    if os.path.exists(filename):
        progress.console.print(f"{os.path.basename(filename)} already exists, skipping.")
        progress.update(task_id, completed=1)
        return

    with session.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        downloaded = 0

        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress.update(task_id, completed=downloaded, total=total_size)

def download_all_parallel(session, tasks, max_workers=5):
    """
    tasks = [(url, folder), ...]
    """

    with Progress(
        TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
        BarColumn(),
        DownloadColumn(),
        TimeRemainingColumn(),
    ) as progress:

        futures = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for url, folder in tasks:
                filename = os.path.basename(url) + ".zip"
                task_id = progress.add_task("download", filename=filename, total=0)

                future = executor.submit(
                    download_file,
                    session,
                    url,
                    folder,
                    progress,
                    task_id
                )
                futures.append(future)

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    progress.console.print(f"Error: {e}")