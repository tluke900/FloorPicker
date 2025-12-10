import os
import urllib.request
import zipfile
from tqdm import tqdm

# ADE20K download URL (official MIT link)
ADE20K_URL = "http://data.csail.mit.edu/places/ADE20K/ADE20K_2021_17_01.zip"

# Destination paths
DATA_DIR = "data"
ZIP_PATH = os.path.join(DATA_DIR, "ADE20K.zip")
EXTRACT_DIR = os.path.join(DATA_DIR, "ADE20K")

# Create data folder
os.makedirs(DATA_DIR, exist_ok=True)

# Progress bar hook
class DownloadProgressBar(tqdm):
    def update_to(self, blocks=1, block_size=1, total_size=None):
        if total_size is not None:
            self.total = total_size
        self.update(blocks * block_size)

def download_ade20k():
    if os.path.exists(EXTRACT_DIR):
        print("ADE20K is already downloaded and extracted.")
        return

    print("Starting ADE20K download...")

    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc="Downloading ADE20K") as t:
        urllib.request.urlretrieve(
            ADE20K_URL,
            ZIP_PATH,
            reporthook=t.update_to
        )

    print("\nDownload complete. Extracting...")

    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(DATA_DIR)

    print("Extraction complete.")
    print(f"ADE20K extracted to: {EXTRACT_DIR}")


if __name__ == "__main__":
    download_ade20k()
