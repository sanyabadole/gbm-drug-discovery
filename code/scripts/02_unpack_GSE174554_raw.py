#!/usr/bin/env python

"""
Script: 02_unpack_GSE174554_raw.py
Purpose: Extract GSE174554_RAW.tar into per-sample folders under data/raw/GSE174554/raw_unpacked

Usage:
    conda activate gbm_env
    python code/scripts/02_unpack_GSE174554_raw.py
"""

from pathlib import Path
import tarfile

GSE_ID = "GSE174554"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw" / GSE_ID
TAR_PATH = RAW_DIR / "GSE174554_RAW.tar"
OUT_DIR = RAW_DIR / "raw_unpacked"


def main():
    print("Project root:", PROJECT_ROOT)
    print("Tar file   :", TAR_PATH)
    print("Output dir :", OUT_DIR)

    if not TAR_PATH.exists():
        raise FileNotFoundError(f"Tar file not found: {TAR_PATH}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Extract tar safely
    with tarfile.open(TAR_PATH, "r") as tar:
        tar.extractall(path=OUT_DIR)

    print("Extraction complete.")
    print("Some extracted files:")
    for p in sorted(OUT_DIR.iterdir())[:10]:
        print("  -", p.name)


if __name__ == "__main__":
    main()
