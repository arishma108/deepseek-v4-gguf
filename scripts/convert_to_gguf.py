#!/usr/bin/env python3
"""
DeepSeek-V4-Flash to GGUF Converter
Author: Darshani Persadh
License: MIT
Repository: https://github.com/arishma108/deepseek-v4-gguf
"""

import subprocess
import os
import argparse
import sys

def convert_to_gguf(model_path, output_path, quant_type="IQ1_S-XL"):
    """
    Convert DeepSeek-V4-Flash to GGUF format.
    
    Args:
        model_path: Path to original Hugging Face model directory
        output_path: Output directory for GGUF shards
        quant_type: Quantization type (IQ1_S-XL, Q2_K-XL, Q4_K_M-XL)
    
    Returns:
        bool: True if conversion succeeded, False otherwise
    """
    
    # Validate input
    if not os.path.exists(model_path):
        print(f"❌ Error: Model path not found: {model_path}")
        return False
    
    if not os.path.exists("llama.cpp"):
        print("❌ Error: llama.cpp not found in current directory")
        print("Please clone llama.cpp first: git clone https://github.com/arishma108/llama.cpp")
        return False
    
    # Build output filename
    output_file = os.path.join(output_path, f"DeepSeek-V4-Flash-{quant_type}.gguf")
    
    # Construct command
    cmd = [
        "python", "llama.cpp/convert_hf_to_gguf.py",
        model_path,
        "--outfile", output_file,
        "--outtype", quant_type.lower(),
        "--vocab-type", "spm"
    ]
    
    print(f"🚀 Running conversion...")
    print(f"   Input: {model_path}")
    print(f"   Output: {output_file}")
    print(f"   Quantization: {quant_type}")
    print(f"   Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ Conversion complete!")
        print(f"   Output: {output_file}")
        
        # Show file size
        if os.path.exists(output_file):
            size_gb = os.path.getsize(output_file) / (1024**3)
            print(f"   Size: {size_gb:.1f} GB")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Conversion failed with error code {e.returncode}")
        print(f"   stdout: {e.stdout}")
        print(f"   stderr: {e.stderr}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Convert DeepSeek-V4-Flash to GGUF format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/DeepSeek-V4-Flash ./output
  %(prog)s /path/to/DeepSeek-V4-Flash ./output --quant Q2_K-XL
  %(prog)s /path/to/DeepSeek-V4-Flash ./output --quant IQ1_S-XL
        """
    )
    
    parser.add_argument("model_path", help="Path to original Hugging Face model directory")
    parser.add_argument("output_path", help="Output directory for GGUF files")
    parser.add_argument("--quant", default="IQ1_S-XL", 
                       help="Quantization type (IQ1_S-XL, Q2_K-XL, Q4_K_M-XL, etc.)")
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_path, exist_ok=True)
    
    # Run conversion
    success = convert_to_gguf(args.model_path, args.output_path, args.quant)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()