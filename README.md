# DeepSeek-V4-Flash-GGUF

**IQ1_S-XL Quantization of DeepSeek-V4-Flash in 2 shards [50GB + 11.6GB] for Consumer Hardware**

[![DOI](https://img.shields.io/badge/DOI-10.57967/hf/8828-blue.svg)](https://doi.org/10.57967/hf/8828)
[![Hugging Face](https://img.shields.io/badge/🤗-Model-yellow.svg)](https://huggingface.co/persadian/DeepSeek-V4-Flash-GGUF)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 📊 Model Details

| Property | Value |
|----------|-------|
| **Base Model** | DeepSeek-V4-Flash (284B parameters, 13B active) |
| **Quantization** | IQ1_S-XL |
| **Total Size** | 61.6 GB (2 shards: 50GB + 11.6GB) |
| **Format** | GGUF (llama.cpp compatible) |
| **Context Length** | 1,048,576 tokens (1M) |
| **Architecture** | Mixture-of-Experts (256 experts) |
| **DOI** | [10.57967/hf/8828](https://doi.org/10.57967/hf/8828) |
| **License** | MIT |

### Quick Start

```bash
# Download from Hugging Face
huggingface-cli download persadian/DeepSeek-V4-Flash-GGUF --local-dir ./model
```

### Run with llama.cpp
```
# Clone V4-aware fork
git clone -b feat/v4-port-cuda https://github.com/arishma108/llama.cpp
cd llama.cpp
make LLAMA_CUDA=1 -j

# Run inference
./llama-cli -m ../model/DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf \
  -p "Explain quantum computing" -n 256 -ngl 35
```

### Run Python (llama-cpp-python)
```
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="persadian/DeepSeek-V4-Flash-GGUF",
    filename="DeepSeek-V4-Flash-IQ1_S-XL-00001-of-00002.gguf",
    n_ctx=8192,
    n_gpu_layers=35
)

response = llm.create_chat_completion(
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response["choices"][0]["message"]["content"])
```
### Hardware Requirements
| Component   | Minimum Requirement | Recommended Configuration |
| ----------- | ------------------- | ------------------------- |
| RAM         | 64 GB               | 128 GB                    |
| VRAM        | 22 GB               | 24 GB (RTX 3090)          |
| Storage     | 150 GB              | 200 GB                    |
| GPU Compute | CUDA 11.0+          | CUDA 12.0+                |

### IP Claim & Provenance
```
This repository contains cryptographic proof of authorship:
-- SHA256_SUMS.txt - Fingerprints of the exact model files
-- IPCLAIM.txt - Timestamped claim of authorship (adapted from IPClaim model)
```
### Citation
```
bibtex
@misc{persadh2026deepseek,
  author = {Persadh, Darshani},
  title = {IQ1_S-XL: A Quantized DeepSeek-V4-Flash for Consumer Hardware},
  year = {2026},
  doi = {10.57967/hf/8828}
}
```
### APA 
Persadh, D. (2026). *IQ1_S-XL: A Quantized DeepSeek-V4-Flash for Consumer Hardware* (IQ1_S-XL) [Model]. Hugging Face. https://doi.org/10.57967/hf/8828

### License
MIT License - see LICENSE file

### Acknowledgments
-- DeepSeek AI for the base model
-- llama.cpp community for GGUF format and V4 support
-- teamblobfish for the original IQ1_S-XL quantization work
-- Hugging Face for hosting infrastructure

### Author 
Darshani Persadh | ORCID: 0009-0007-5932-1262 | @persadian

**[DeepSeek-V4-Flash-GGUF](https://github.com/arishma108/deepseek-v4-gguf)** - my quantized model release (61.6GB, IQ1_S-XL)

---









