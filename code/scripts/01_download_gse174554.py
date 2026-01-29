#!/usr/bin/env python

"""
Script: 01_download_gse174554.py
Purpose: Download GSE174554 raw and processed files into data/raw/
Usage:
    conda activate gbm_env
    python code/scripts/01_download_gse174554.py
"""

import os
from pathlib import Path
import urllib.request

# ----------- config -----------

GSE_ID = "GSE174554"

# URLs for key files (from GEO)
URLS = {
    "GSE174554_RAW.tar": (
        "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE174554&format=file"
    ),
    "GSE174554_Spatial_transcriptomic_matrix.txt.gz": (
        "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE174nnn/GSE174554/suppl/"
        "GSE174554_Spatial_transcriptomic_matrix.txt.gz"
    ),
    "GSE174554_Tumor_normal_metadata.txt.gz": (
        "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE174nnn/GSE174554/suppl/"
        "GSE174554_Tumor_normal_metadata.txt.gz"
    ),
}

# ----------- paths -----------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PROJECT_ROOT / "data" / "raw" / GSE_ID
DATA_RAW.mkdir(parents=True, exist_ok=True)

# ----------- helpers -----------

def download_file(url: str, dest: Path) -> None:
    """Download url to dest if not already present."""
    if dest.exists():
        print(f"[skip] {dest.name} already exists")
        return

    print(f"[download] {dest.name} from {url}")
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"[done] {dest}")
    except Exception as e:
        print(f"[error] failed to download {dest.name}: {e}")


# ----------- main -----------

def main():
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Downloading into: {DATA_RAW}\n")

    for filename, url in URLS.items():
        out_path = DATA_RAW / filename
        download_file(url, out_path)

    print("\nAll downloads attempted.")
    print(f"Files in {DATA_RAW}:")
    for f in sorted(DATA_RAW.iterdir()):
        print("  -", f.name)


if __name__ == "__main__":
    main()
