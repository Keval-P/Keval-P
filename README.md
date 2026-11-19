# Keval Pandya

AI/ML engineer in Ahmedabad, India. I work on computer vision and edge inference: getting models to run fast and
correctly on NVIDIA Jetson and RTX GPUs with TensorRT, building multi-camera video pipelines in DeepStream and
GStreamer, and moving pre- and post-processing onto the GPU with CUDA.

## What I work on

- **Model optimisation.** PyTorch to ONNX to TensorRT, FP16 and INT8 engines, and checking each engine's accuracy
  against the FP32 model before it is used.
- **GPU video pipelines.** Hardware decode, batching, inference and tracking in DeepStream and GStreamer, with
  frames kept in GPU memory from decode to inference.
- **CUDA pre- and post-processing.** Resize, letterbox and decode steps written with PyCUDA and CV-CUDA instead of
  CPU code.
- **Model changes for edge hardware.** ONNX graph surgery, small-object detection heads, and replacing layers that
  a target device cannot compile.

## Currently building

These are being prepared as public repositories and will be linked here when they are released.

- **YOLO26 runtime comparison on Jetson Orin Nano.** The same model taken step by step from the default PyTorch
  model through ONNX Runtime, TensorRT and custom CUDA kernels (PyCUDA, CV-CUDA) to native C++ CUDA.
- **DeepStream line-crossing counter.** Detection, tracking and counting objects that cross a line.
- **TensorRT FP32 / FP16 / INT8 check.** Three engines from one ONNX model, compared for speed and accuracy.
- **Learning projects.** A set of DeepStream, GPU-pipeline and Kubernetes projects being cleaned up for release.

## Open source and community

- [AI Stack Exchange](https://ai.stackexchange.com/users/78733/keval-pandya): 32 answers, 676 reputation, mostly on
  machine learning, neural networks and GPU questions.
- [samson-wang/cython_bbox#14](https://github.com/samson-wang/cython_bbox/pull/14): open pull request replacing the
  removed `np.float` alias with `np.float64` so the package builds on current NumPy. The same fix is in
  [my fork](https://github.com/Keval-P/cython_bbox).

## Stack

- **Inference:** TensorRT, ONNX, ONNX Runtime, TensorRT-LLM, Triton Inference Server
- **Video:** DeepStream, GStreamer, NVDEC, CV-CUDA, PyCUDA
- **Hardware:** Jetson Orin Nano, Orin NX, AGX Orin and AGX Xavier, RTX GPUs, Coral Edge TPU
- **Training and serving:** PyTorch, multi-GPU DDP, MLflow, QLoRA fine-tuning of vision-language models, FastAPI,
  Docker, Kubernetes

## Certification

- NVIDIA-Certified Associate: Generative AI and LLMs (2026)

## Elsewhere

- Portfolio: [keval-p.github.io](https://keval-p.github.io/)
- Questions and answers: [AI Stack Exchange](https://ai.stackexchange.com/users/78733/keval-pandya)
