#!/usr/bin/env python3
"""
Verify DeepSeek-V4-Flash GGUF shards using SHA256
Author: Darshani Persadh
License: MIT
Repository: https://github.com/arishma108/deepseek-v4-gguf
"""

import hashlib
import os
import sys
import json
from pathlib import Path

# Expected SHA256 hashes - UPDATE THESE with actual values from Hugging Face
EXPECTED_HASHES = {
    "DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf": "SHA256:
3edd21794e285c6cdb1ea6cf030b724e5d91843d00762e9e2daf789a86d0d227",
    "DeepSeek-V4-Flash-IQ1_S-XL-00002-of-00002.gguf": "SHA256:
b15ce53183f61b8f29a9ccfd5b132a2577b3db82191cac49ebf3ca7e541495b5",
}

def calculate_sha256(filepath):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    
    with open(filepath, "rb") as f:
        # Read file in 64KB chunks to handle large files
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    
    return sha256_hash.hexdigest()

def verify_file(filepath):
    """Verify a single file against expected hash."""
    filename = os.path.basename(filepath)
    
    if filename not in EXPECTED_HASHES:
        print(f"⚠️  No expected hash recorded for: {filename}")
        return False
    
    expected = EXPECTED_HASHES[filename]
    
    print(f"   Calculating SHA256 for {filename}...")
    calculated = calculate_sha256(filepath)
    
    if calculated == expected:
        print(f"   ✅ {filename}: OK")
        return True
    else:
        print(f"   ❌ {filename}: MISMATCH")
        print(f"      Expected: {expected}")
        print(f"      Got:      {calculated}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python verify_shards.py <model_directory>")
        print("")
        print("Example:")
        print("  python verify_shards.py ./downloaded_model")
        print("")
        print("This script verifies the integrity of downloaded model shards")
        print("by comparing their SHA256 hashes against the expected values.")
        sys.exit(1)
    
    model_dir = sys.argv[1]
    
    if not os.path.exists(model_dir):
        print(f"❌ Directory not found: {model_dir}")
        sys.exit(1)
    
    print(f"🔍 Verifying model files in: {model_dir}")
    print("")
    
    all_ok = True
    files_found = 0
    
    for filename in EXPECTED_HASHES:
        filepath = os.path.join(model_dir, filename)
        
        if os.path.exists(filepath):
            files_found += 1
            if not verify_file(filepath):
                all_ok = False
        else:
            print(f"❌ Missing: {filename}")
            all_ok = False
    
    print("")
    print(f"Found {files_found} of {len(EXPECTED_HASHES)} expected files")
    
    if all_ok and files_found == len(EXPECTED_HASHES):
        print("")
        print("✅✅✅ ALL FILES VERIFIED SUCCESSFULLY! ✅✅✅")
        print("The model files are authentic and uncorrupted.")
        sys.exit(0)
    else:
        print("")
        print("❌ Verification failed. Please check the files above.")
        sys.exit(1)

if __name__ == "__main__":
    main()