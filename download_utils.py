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
    """Inicia sessão e retorna objeto requests.Session()"""
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
    print("✅ Login feito")
    return session

def download_file(session, url, folder, progress, task_id):
    """Baixa arquivo com barra de progresso Rich"""
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, url.split("/")[-1] + ".zip")

    if os.path.exists(filename):
        progress.console.print(f"⚠️ {os.path.basename(filename)} já existe, pulando.")
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

def download_batch(session, urls, folder):
    """Baixa até 3 arquivos em paralelo com barras de progresso separadas"""
    threads = []
    with Progress(
        TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
        BarColumn(),
        DownloadColumn(),
        TimeRemainingColumn(),
    ) as progress:
        task_map = {}
        for url in urls:
            filename = os.path.basename(url) + ".zip"
            task_id = progress.add_task("download", filename=filename, total=0)
            task_map[url] = task_id

        for url in urls:
            t = threading.Thread(target=download_file, args=(session, url, folder, progress, task_map[url]))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

def download_parallel(session, urls, folder, max_workers=5):
    """Baixa arquivos em paralelo contínuo (máx N simultâneos)"""

    with Progress(
        TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
        BarColumn(),
        DownloadColumn(),
        TimeRemainingColumn(),
    ) as progress:

        futures = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for url in urls:
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

            # espera todos terminarem
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    progress.console.print(f"❌ Erro: {e}")