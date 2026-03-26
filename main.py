# main.py
import os
from credentials import USERNAME, PASSWORD
from download_utils import start_session, download_batch, BASE_URL

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

for name, ids in datasets.items():
    print(f"\n📂 Baixando {name}...")
    folder = os.path.join(BASE_DIR, name)
    urls = [BASE_URL + str(i) for i in ids]

    # divide em blocos de 3 arquivos
    for i in range(0, len(urls), 3):
        batch = urls[i:i+3]
        print(f"⬇️ Lote: {batch}")
        download_batch(session, batch, folder)

print("\n🎉 Todos downloads finalizados!")