# check_downloads.py
import os
import zipfile

# ===== CONFIG =====
BASE_DIR = "downloads/"  # pasta onde os downloads foram salvos

# Estrutura de datasets com IDs usados para gerar nomes de arquivo
datasets = {
    "skeletons": [158],
    "masked_depth": list(range(82, 111, 2)),
    "full_depth": [42] + list(range(159, 173)),
    "rgb_videos": list(range(142, 157)),
    "ir_videos": [105,107,109,113,115,117,119,40,45,43,120,121,122,123,124],
    "auth_uav": [221],
    "tvbench": [230]
}

def is_zip_complete(file_path):
    """Verifica se o arquivo zip está íntegro"""
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            bad_file = zf.testzip()
            if bad_file:
                return False
        return True
    except zipfile.BadZipFile:
        return False
    except Exception:
        return False

def check_downloads():
    incomplete_files = []
    complete_files = []

    for name, ids in datasets.items():
        folder = os.path.join(BASE_DIR, name)
        for file_id in ids:
            filename = os.path.join(folder, f"{file_id}.zip")
            
            if not os.path.exists(filename):
                incomplete_files.append((filename, "Arquivo não existe"))
                continue
            
            if os.path.getsize(filename) == 0:
                incomplete_files.append((filename, "Arquivo vazio"))
                continue
            
            # verifica integridade do zip
            if not is_zip_complete(filename):
                incomplete_files.append((filename, "ZIP corrompido ou incompleto"))
            else:
                complete_files.append(filename)
    
    print("\n📊 Verificação de arquivos concluída")
    print(f"✅ Arquivos completos: {len(complete_files)}")
    for f in complete_files:
        print(f"   {f}")
    print(f"❌ Arquivos incompletos: {len(incomplete_files)}")
    for f, reason in incomplete_files:
        print(f"   {f} | {reason}")

if __name__ == "__main__":
    check_downloads()