import os
from credentials import USERNAME, PASSWORD
from download_utils import start_session, download_all_parallel, BASE_URL

BASE_DIR = "downloads/"

datasets = {
    "skeletons": [158],
    "masked_depth": list(range(82, 111, 2)),
    "full_depth": [42] + list(range(159, 173)),
    "rgb_videos": list(range(142, 157)),
    "ir_videos": [105,107,109,113,115,117,119,40,45,43,120,121,122,123,124],
    "auth_uav": [221],
    "tvbench": [230]
}

session = start_session(USERNAME, PASSWORD)

tasks = []

for name, ids in datasets.items():
    folder = os.path.join(BASE_DIR, name)
    urls = [BASE_URL + str(i) for i in ids]

    for url in urls:
        tasks.append((url, folder))

print(f"All files: {len(tasks)}")
print("Starting downloads...\n")

download_all_parallel(session, tasks, max_workers=5)

print("\n All files downloaded!")