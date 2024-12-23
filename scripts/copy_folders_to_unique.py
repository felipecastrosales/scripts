import os
import shutil
from tqdm import tqdm

def copy_files_to_unique_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Criada a pasta de destino: {destination_folder}")

    # List all files in the source folder and subfolders
    all_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            all_files.append(os.path.join(root, file))
    print(f"Total de arquivos encontrados: {len(all_files)}")

    # Copy each file to the destination folder
    for file in tqdm(all_files, desc="Copying files"):
        shutil.copy(file, destination_folder)
        print(f"Copiado: {file}")

if __name__ == "__main__":
    source_folder = "/Volumes/FLASHDEVICE"  # Caminho da pasta de origem
    destination_folder = "/Volumes/FLASHDEVICE/fabricio"  # Caminho da pasta de destino

    print("Iniciando a cópia dos arquivos...")
    copy_files_to_unique_folder(source_folder, destination_folder)
    print("Cópia concluída.")
