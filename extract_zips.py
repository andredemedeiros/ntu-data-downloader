from pathlib import Path
import zipfile

BASE_DIR = Path("downloads/")

DATASETS = {
    "skeletons": [157, 158],
    "masked_depth": list(range(48, 53, 2)) + list(range(82, 87, 2)),
    "rgb_videos": list(range(125, 128)) + list(range(142, 145)),
    "ir_videos": list(range(71, 76, 2)) + [105, 107, 109],
    "auth_uav": [221],
    "tvbench": [230]
}

total = sum(len(v) for v in DATASETS.values())
count = 0
errors = []

for dataset, ids in DATASETS.items():
    print(f"\n[ {dataset} ]")

    for file_id in ids:
        count += 1

        zip_path = BASE_DIR / dataset / f"{file_id}.zip"
        extract_dir = BASE_DIR / dataset / str(file_id)

        if not zip_path.exists():
            print(
                f"  [{count:>2}/{total}] ✘  {dataset}/{file_id}.zip  →  ZIP NOT FOUND"
            )
            errors.append((dataset, file_id, "ZIP NOT FOUND"))
            continue

        # pula se a pasta já existe e não está vazia
        if extract_dir.exists() and any(extract_dir.iterdir()):
            print(
                f"  [{count:>2}/{total}] ↷  {dataset}/{file_id}.zip  →  ALREADY EXTRACTED"
            )
            continue

        try:
            extract_dir.mkdir(parents=True, exist_ok=True)

            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(extract_dir)

            print(
                f"  [{count:>2}/{total}] ✔  {dataset}/{file_id}.zip  →  extracted to {extract_dir}"
            )

        except zipfile.BadZipFile:
            print(
                f"  [{count:>2}/{total}] ⚠  {dataset}/{file_id}.zip  →  INVALID ZIP"
            )
            errors.append((dataset, file_id, "INVALID ZIP"))

        except Exception as e:
            print(
                f"  [{count:>2}/{total}] ⚠  {dataset}/{file_id}.zip  →  ERROR: {e}"
            )
            errors.append((dataset, file_id, str(e)))

print(f"\n{'─'*60}")
print(f"Extraction errors: {len(errors)}/{total}")

if errors:
    print("\nFailed files:")
    for dataset, file_id, reason in errors:
        print(f"  {dataset}/{file_id}.zip\t{reason}")