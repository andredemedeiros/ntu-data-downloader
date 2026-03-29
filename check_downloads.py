from pathlib import Path
from credentials import USERNAME, PASSWORD
from download_utils import start_session, BASE_URL

BASE_DIR = Path("downloads/")

datasets = {
    "skeletons": [157,158],
    "masked_depth": [list(range(48, 81, 2)),list(range(82, 111, 2))],
    #"full_depth": [42] + list(range(159, 173)),
    "rgb_videos": [list(range(125, 142)),list(range(142, 157))],
    "ir_videos": [list(range(71, 104)),105,107,109,113,115,117,119,40,45,43,120,121,122,123,124],
    "auth_uav": [221],
    "tvbench": [230]
}

def get_remote_size(session, url):
    """Sends a HEAD request and returns the server's Content-Length."""
    try:
        r = session.head(url, timeout=15)
        r.raise_for_status()
        return int(r.headers.get("content-length", -1))
    except Exception as e:
        return None

def human_size(b):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if b < 1024:
            return f"{b:.2f} {unit}"
        b /= 1024

def check(session, dataset, file_id):
    local = BASE_DIR / dataset / f"{file_id}.zip"
    url   = BASE_URL + str(file_id)

    if not local.exists():
        return "ABSENT", None, None

    local_size  = local.stat().st_size
    remote_size = get_remote_size(session, url)

    if remote_size is None:
        return "SERVER_ERROR", local_size, None

    if remote_size == -1:
        return "NO_CONTENT_LENGTH", local_size, remote_size

    if local_size == remote_size:
        return "OK", local_size, remote_size
    elif local_size < remote_size:
        return "INCOMPLETE", local_size, remote_size
    else:
        return "GREATER_THAN_EXPECTED", local_size, remote_size

session = start_session(USERNAME, PASSWORD)

problems = []
total = sum(len(v) for v in DATASETS.values())
count = 0

for ds, ids in DATASETS.items():
    print(f"\n[ {ds} ]")
    for fid in ids:
        count += 1
        status, local_sz, remote_sz = check(session, ds, fid)

        if status == "OK":
            mark = "✔"
            info = f"{human_size(local_sz)}"
        elif status == "ABSENT":
            mark = "✘"
            info = "file not found"
        elif status == "INCOMPLETE":
            pct  = local_sz / remote_sz * 100
            mark = "✘"
            info = f"{human_size(local_sz)} de {human_size(remote_sz)} ({pct:.1f}%)"
        elif status == "NO_CONTENT_LENGTH":
            mark = "?"
            info = f"server didn't provide the length — local: {human_size(local_sz)}"
        elif status == "SERVER_ERROR":
            mark = "?"
            info = f"error from the server response — local: {human_size(local_sz)}"
        else:
            mark = "⚠"
            info = f"local {human_size(local_sz)} > remote {human_size(remote_sz)}"

        print(f"  [{count:>2}/{total}] {mark}  {ds}/{fid}.zip  →  {status}  {info}")

        if status not in ("OK"):
            problems.append(f"{ds}\t{fid}\t{status}")

print(f"\n{'─'*55}")
print(f"Problems: {len(problems)}/{total}")