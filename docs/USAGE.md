# Detailed Usage Guide for DeepSeek-V4-Flash-GGUF

## Prerequisites

### Hardware Requirements
- **RAM:** 64GB minimum (128GB recommended)
- **Storage:** 150GB free space
- **GPU (optional):** NVIDIA GPU with 22GB+ VRAM (RTX 3090 or better)

### Software Requirements
- **llama.cpp** with V4 support (clone from `arishma108/llama.cpp`)
- **CUDA Toolkit** 11.0+ (for GPU acceleration)
- **Python** 3.9+ (for Python bindings)

## Installation

### 1. Clone and Build llama.cpp

```bash
# Clone the V4-aware fork
git clone -b feat/v4-port-cuda https://github.com/arishma108/llama.cpp
cd llama.cpp

# Build with CUDA support
mkdir build && cd build
cmake .. -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)