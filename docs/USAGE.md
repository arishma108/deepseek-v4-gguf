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
```
### 2. Download the Model

```bash
# Using huggingface-cli
huggingface-cli download persadian/DeepSeek-V4-Flash-GGUF --local-dir ./model

# Or using wget
wget https://huggingface.co/persadian/DeepSeek-V4-Flash-GGUF/resolve/main/DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf
wget https://huggingface.co/persadian/DeepSeek-V4-Flash-GGUF/resolve/main/DeepSeek-V4-Flash-IQ1_S-XL-00002-of-00002.gguf
```
### 3. Verify Model Integrity
```
python scripts/verify_shards.py ./model
```
## Running Inference
### Command Line (llama-cli)
```
# Basic text generation
./llama-cli -m ./model/DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf \
  -p "Explain quantum computing" \
  -n 256 \
  -c 4096 \
  -ngl 35

# Interactive chat mode
./llama-cli -m ./model/DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf \
  --color \
  --interactive \
  --reverse-prompt "User:" \
  --in-prefix " " \
  --in-suffix "Assistant:"
```
### HTTP Server (llama-server)
```
# Start API server
./llama-server -m ./model/DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf \
  --host 0.0.0.0 \
  --port 8080 \
  --n-gpu-layers 35

# Query the API
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Hello!"}],
    "max_tokens": 100
  }'
```
### Python (llama-cpp-python)
```
from llama_cpp import Llama

# Initialize model
llm = Llama(
    model_path="./model/DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf",
    n_ctx=8192,
    n_gpu_layers=35,
    verbose=False
)

# Generate completion
output = llm(
    "Q: What is machine learning?\nA:",
    max_tokens=256,
    stop=["Q:", "\n"],
    echo=True
)

print(output["choices"][0]["text"])
```
## Performance Optimization
### GPU Memory Tuning
```bash
# Reduce GPU layers
-ngl 20

# Reduce context size
-c 2048

# Use CPU only
-ngl 0
```
### Batch Processing
For processing multiple prompts efficiently:
```
./llama-cli -m model.gguf \
  --batch-size 512 \
  --ubatch-size 512 \
  --threads 16
```
## Troubleshooting
### Error: "model must be loaded with the first split"
Cause: You're trying to load the second shard directly.
Fix: Always point to -00001-of-00002.gguf (the first shard).

### Error: "CUDA out of memory"
Fix: Reduce -ngl value or -c context size.

### Error: "llama.cpp: error loading model"
Fix: Verify the model files with verify_shards.py script.

## Additional Resources
[Hugging Face Model Page] (https://huggingface.co/persadian/DeepSeek-V4-Flash-GGUF)
[arXiv Paper] (https://doi.org/10.57967/hf/8828)
[llama.cpp Documentation] (https://github.com/ggerganov/llama.cpp)












