---
title: LM Studio, Ollama, llama.cpp, Lemonade
xp: 25
---
# Same engine, different packaging

> **Warm-up:** you've used LM Studio and Lemonade. What do you think is actually *different* between them, and what is the same?

Most local runners are wrappers around the same few engines:

| Runner | What it is | Engine(s) | API port (default) |
|---|---|---|---|
| **llama.cpp** | The C/C++ engine itself. `llama-cli` to chat in a terminal, `llama-server` for an API with a small web UI. | itself | 8080 |
| **LM Studio** | Desktop app: model browser, chat UI, server, `lms` command line tool. Closed source, free. | llama.cpp (+ MLX on Macs) | 1234 |
| **Ollama** | Command line + background service, its own model library (`ollama run qwen3:8b`). Open source. | its own engine built on GGML (llama.cpp's library) | 11434 |
| **Lemonade** | AMD's open-source local server, aimed at Ryzen AI NPUs and Radeon GPUs. | llama.cpp (Vulkan/ROCm), ONNX Runtime for NPUs | see its docs |
| **vLLM**, **SGLang** | High-throughput servers for many users at once. Mostly NVIDIA, some ROCm support. Use safetensors, not GGUF. | their own | 8000 |

What really differs: model management, how settings are exposed, which GPU backends are bundled, and update speed. The same GGUF with the same settings gives very similar output and speed in all llama.cpp-based runners. When a brand-new model architecture appears, **llama.cpp supports it first**, and the wrappers follow when they update their bundled copy.

All of them speak the **OpenAI-compatible API**: the same HTTP requests work against any of them, only the address changes. That's why other tools (editors, agents, scripts) can use "your local model" without caring which runner you chose.

On NixOS, nixpkgs has `lmstudio`, `ollama` (plus `services.ollama` with an `acceleration` option) and `llama-cpp`. Version numbers in nixpkgs can lag behind upstream; `nix search nixpkgs llama-cpp` shows what you'd get.

## Your quest

1. Fill in `PORTS` with the default ports of `"lmstudio"`, `"ollama"` and `"llamacpp"`.
2. Write `base_url(runner)`: return `"http://localhost:PORT/v1"` for that runner. An f-string does it: `f"http://localhost:{port}/v1"`.

## Review

<details><summary>What decides an MoE model's speed, and what decides its memory?</summary>Speed: the active parameters per token. Memory: the total parameters.</details>
<details><summary>Roughly how fast can a 4.9 GB model generate on a 384 GB/s GPU?</summary>At most about 384 / 4.9 ≈ 78 tokens/s, in practice 60–80% of that.</details>
