<p align="center"><img src="assets/header.svg" alt="Keval Pandya, AI/ML Engineer, GPU Inference and Edge AI" width="100%" /></p>

<h1 align="center">Keval Pandya</h1>


<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=600&size=21&duration=2800&pause=900&color=DC1D47&center=true&vCenter=true&width=820&lines=I+turn+AI+models+into+reliable+real-time+systems;PyTorch+%E2%86%92+ONNX+%E2%86%92+TensorRT+%E2%86%92+production;Multi-camera+pipelines+on+Jetson+and+RTX;Frames+stay+on+the+GPU%2C+from+decode+to+inference" alt="I turn AI models into reliable real-time systems" /></p>

<p align="center">
<a href="https://keval-p.github.io/"><img alt="Keval Pandya portfolio" src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&labelColor=000000&logo=githubpages&logoColor=DC1D47" /></a>
<a href="https://www.linkedin.com/in/keval-pandya-ai-ml-engineer"><img alt="Keval Pandya on LinkedIn" src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&labelColor=000000&logo=linkedin&logoColor=DC1D47" /></a>
<a href="https://ai.stackexchange.com/users/78733/keval-pandya"><img alt="Keval Pandya on AI Stack Exchange" src="https://img.shields.io/badge/AI_Stack_Exchange-000000?style=for-the-badge&labelColor=000000&logo=stackexchange&logoColor=DC1D47" /></a>
<a href="https://github.com/Keval-P"><img alt="Keval Pandya on GitHub" src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&labelColor=000000&logo=github&logoColor=DC1D47" /></a>
</p>

<p align="center"><img src="https://komarev.com/ghpvc/?username=Keval-P&label=Profile+Views&color=DC1D47&style=for-the-badge&labelColor=000000" alt="Profile views" /></p>

<h2>👋 About</h2>

<p><b>Keval Pandya</b> is an AI/ML engineer in Ahmedabad, India, with 3 years of experience designing, developing and deploying
production AI systems across computer vision, GPU inference and edge AI. I have developed and deployed 15+ AI solutions
across industrial automation, logistics, safety monitoring and face recognition, working end to end: model development,
inference optimisation and real-time multi-camera systems with PyTorch, ONNX, TensorRT, PyCUDA, DeepStream and GStreamer,
plus VLM fine-tuning and LLM/RAG applications.</p>

<table align="center">
  <tr>
    <td align="center"><h3>15+</h3>AI solutions delivered</td>
    <td align="center"><h3>5 → 20 cameras</h3>on a single Jetson Orin Nano</td>
    <td align="center"><h3>24 → 60 FPS</h3>gate automation throughput</td>
    <td align="center"><h3>5 s → 500 ms</h3>per frame on Jetson Orin NX</td>
  </tr>
</table>

<h2>⚙️ What I do</h2>
<ul>
  <li><b>Computer vision and edge AI, end to end.</b> Model training, PyTorch-to-ONNX conversion, TensorRT optimisation and hardware-specific rollout on RTX GPUs, NVIDIA Jetson, NPUs and Raspberry Pi.</li>
  <li><b>GPU inference optimisation.</b> Profiling with Nsight Systems, Nsight Compute and trtexec; keeping frames on the GPU from NVDEC decode through pre- and post-processing; pinned memory, CUDA streams and preallocated GPU buffers to raise throughput and control VRAM.</li>
  <li><b>Model and graph work.</b> ONNX graph changes (node fusion, operator simplification, dynamic-shape fixes), FP32/FP16 TensorRT engines, and accuracy checks against the FP32 baseline before deployment.</li>
  <li><b>Multi-camera pipelines.</b> DeepStream and GStreamer pipelines with detection, tracking, re-identification, OCR and face recognition, in Python and C++.</li>
  <li><b>Edge-to-cloud architecture.</b> Multi-camera inference and event processing with Docker, Kubernetes, NVIDIA GPU Operator, RabbitMQ, Kafka, Redis and MongoDB.</li>
  <li><b>VLM and LLM systems.</b> Vision-language model fine-tuning with 4-bit quantisation (Unsloth), LLM/RAG services with FastAPI, Qdrant and FAISS, tracking with MLflow and W&amp;B.</li>
</ul>

<h2>🚀 Selected work</h2>

<table>
  <thead>
    <tr><th align="left">Project</th><th align="left">What it does</th><th align="left">Result</th><th align="left">Stack</th></tr>
  </thead>
  <tbody>
    <tr><td><b>Logistics yard &amp; gate automation</b></td><td>Multi-camera gate system: vehicle detection, container classification, OCR, damage inspection and VLM metadata extraction</td><td><b>24 → 60 FPS</b> gate, 2 → 10 FPS yard; accuracy 85% → 95%</td><td>TensorRT · PyCUDA · VLM · RTX &amp; Jetson</td></tr>
    <tr><td><b>Danger zone monitoring</b></td><td>Real-time industrial safety: detection, tracking and polygon zones that stop machinery on intrusion</td><td><b>5 → 20 cameras</b>, 3 → 10 FPS on one Orin Nano; CPU −60%, VRAM ~7 GB → 3–4 GB</td><td>Jetson Orin · GStreamer · PyCUDA</td></tr>
    <tr><td><b>Multi-camera face recognition</b></td><td>Detection, alignment, embeddings, vector search and anti-spoofing with custom-trained models</td><td>Migrated <b>Python → C++</b> with native threads and preallocated buffers</td><td>ONNX Runtime · TensorRT · Qdrant · FAISS · C++</td></tr>
    <tr><td><b>Industrial anomaly detection</b></td><td>Custom model for small-object and surface-defect detection</td><td>Accuracy 78% → 95%; <b>5 s → 500 ms</b> per frame</td><td>Model architecture · Jetson Orin NX</td></tr>
    <tr><td><b>Automatic number plate recognition</b></td><td>Plate detection with rectification, CTC recognition, multi-frame voting; autoscaled event workers</td><td>Accuracy <b>70% → 95–98%</b>; 3–5 → 11 FPS per camera</td><td>TensorRT · OCR · Kubernetes · KEDA</td></tr>
    <tr><td><b>Object detection &amp; counting</b></td><td>Multi-camera DeepStream pipeline with tracking IDs and line-crossing counts</td><td><b>7 → 15 FPS</b> on a 4 GB Jetson</td><td>DeepStream · TensorRT FP16</td></tr>
    <tr><td><b>Digital twin monitoring</b></td><td>Live person positions on a facility floor map with face recognition and cross-camera re-identification</td><td>Per-camera homography calibration and custom cross-camera association</td><td>CUDA · Re-ID · Face recognition</td></tr>
  </tbody>
</table>

<h2>🧰 Skills</h2>

<h3>📁 Programming Languages</h3>
<div>
<img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&labelColor=000000&logo=python&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/C-000000?style=for-the-badge&labelColor=000000&logo=c&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/CPP-000000?style=for-the-badge&labelColor=000000&logo=cplusplus&logoColor=DC1D47" />
</div>

<h3>🤖 Deep Learning Frameworks</h3>
<div>
<img src="https://img.shields.io/badge/PyTorch-000000?style=for-the-badge&labelColor=000000&logo=pytorch&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/PyTorch-Lightning-000000?style=for-the-badge&labelColor=000000&logo=pytorchlightning&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/TensorFlow-000000?style=for-the-badge&labelColor=000000&logo=tensorflow&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/TensorFlow-Lite-000000?style=for-the-badge&labelColor=000000&logo=tensorflow&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/PaddlePaddle-000000?style=for-the-badge&labelColor=000000&logo=paddlepaddle&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/DeepSpeed-000000?style=for-the-badge&labelColor=000000&logo=deepspeed&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Unsloth-000000?style=for-the-badge&labelColor=000000&logo=unsloth&logoColor=DC1D47" />
</div>

<h3>⚡ Model Optimization &amp; Inference</h3>
<div>
<img src="https://img.shields.io/badge/TensorRT-000000?style=for-the-badge&labelColor=000000&logo=nvidia&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Triton-000000?style=for-the-badge&labelColor=000000&logo=triton&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Numba-000000?style=for-the-badge&labelColor=000000&logo=numba&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/CuPy-000000?style=for-the-badge&labelColor=000000&logo=cupy&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/ONNX-000000?style=for-the-badge&labelColor=000000&logo=onnx&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/ONNX-Runtime-000000?style=for-the-badge&labelColor=000000&logo=onnx&logoColor=DC1D47" />
</div>

<h3>👁️ Computer Vision &amp; Media</h3>
<div>
<img src="https://img.shields.io/badge/OpenCV-000000?style=for-the-badge&labelColor=000000&logo=opencv&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Pillow-000000?style=for-the-badge&labelColor=000000&logo=python&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/DeepStream-000000?style=for-the-badge&labelColor=000000&logo=nvidia&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/GStreamer-000000?style=for-the-badge&labelColor=000000&logo=gstreamer&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/PaddleOCR-000000?style=for-the-badge&labelColor=000000&logo=paddlepaddle&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/CNN-000000?style=for-the-badge&labelColor=000000&logo=python&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/LSTM-000000?style=for-the-badge&labelColor=000000&logo=python&logoColor=DC1D47" />
</div>

<h3>💬 NLP &amp; LLM</h3>
<div>
<img src="https://img.shields.io/badge/HuggingFace-000000?style=for-the-badge&labelColor=000000&logo=huggingface&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Transformers-000000?style=for-the-badge&labelColor=000000&logo=huggingface&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/NLTK-000000?style=for-the-badge&labelColor=000000&logo=nltk&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/NLP-000000?style=for-the-badge&labelColor=000000&logo=python&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/LLM-000000?style=for-the-badge&labelColor=000000&logo=openai&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/VLM-000000?style=for-the-badge&labelColor=000000&logo=openai&logoColor=DC1D47" />
</div>

<h3>📊 Data Science &amp; Numerical Computing</h3>
<div>
<img src="https://img.shields.io/badge/NumPy-000000?style=for-the-badge&labelColor=000000&logo=numpy&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Scikit-Learn-000000?style=for-the-badge&labelColor=000000&logo=scikit-learn&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Matplotlib-000000?style=for-the-badge&labelColor=000000&logo=plotly&logoColor=DC1D47" />
</div>

<h3>🌐 Python Frameworks</h3>
<div>
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&labelColor=000000&logo=flask&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&labelColor=000000&logo=fastapi&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Streamlit-000000?style=for-the-badge&labelColor=000000&logo=streamlit&logoColor=DC1D47" />
</div>

<h3>🗄️ Databases</h3>
<div>
<img src="https://img.shields.io/badge/MongoDB-000000?style=for-the-badge&labelColor=000000&logo=mongodb&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Qdrant-000000?style=for-the-badge&labelColor=000000&logo=qdrant&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Redis-000000?style=for-the-badge&labelColor=000000&logo=redis&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/SQLite-000000?style=for-the-badge&labelColor=000000&logo=sqlite&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/SQL-000000?style=for-the-badge&labelColor=000000&logo=mysql&logoColor=DC1D47" />
</div>

<h3>📦 Messaging</h3>
<div>
<img src="https://img.shields.io/badge/RabbitMQ-000000?style=for-the-badge&labelColor=000000&logo=rabbitmq&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Kafka-000000?style=for-the-badge&labelColor=000000&logo=apachekafka&logoColor=DC1D47" />
</div>

<h3>🔧 CI/CD &amp; Version Control</h3>
<div>
<img src="https://img.shields.io/badge/Github-000000?style=for-the-badge&labelColor=000000&logo=github&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Github-Actions-000000?style=for-the-badge&labelColor=000000&logo=github-actions&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Github-CI-000000?style=for-the-badge&labelColor=000000&logo=github-actions&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Git-000000?style=for-the-badge&labelColor=000000&logo=git&logoColor=DC1D47" />
</div>

<h3>💻 DevOps &amp; Tools</h3>
<div>
<img src="https://img.shields.io/badge/Docker-000000?style=for-the-badge&labelColor=000000&logo=docker&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Docker-Compose-000000?style=for-the-badge&labelColor=000000&logo=docker&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Kubernetes-000000?style=for-the-badge&labelColor=000000&logo=kubernetes&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Linux-000000?style=for-the-badge&labelColor=000000&logo=linux&logoColor=DC1D47" />
</div>

<h3>☁️ Cloud Providers</h3>
<div>
<img src="https://img.shields.io/badge/AWS-000000?style=for-the-badge&labelColor=000000&logo=amazonaws&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Google-Cloud-000000?style=for-the-badge&labelColor=000000&logo=googlecloud&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/PaperSpace-000000?style=for-the-badge&labelColor=000000&logo=paperspace&logoColor=DC1D47" />
</div>

<h3>🖥️ Hardware</h3>
<div>
<img src="https://img.shields.io/badge/Nvidia-Jetson-000000?style=for-the-badge&labelColor=000000&logo=nvidia&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Nvidia-GPU-000000?style=for-the-badge&labelColor=000000&logo=nvidia&logoColor=DC1D47" />
<img src="https://img.shields.io/badge/Raspberry-Pi-000000?style=for-the-badge&labelColor=000000&logo=raspberrypi&logoColor=DC1D47" />
</div>

<h2>🏅 Experience, certifications and community</h2>
<ul>
  <li><b>AI/ML Engineer</b>, WebOccult Technologies Pvt. Ltd., Ahmedabad (Nov 2023 – present). The Visionary award, March 2026.</li>
  <li>NVIDIA-Certified Associate: Generative AI and LLMs (NCA-GENL), 2026</li>
  <li>TensorFlow Developer Certificate, 2024 · AI Programming with Python Nanodegree, Udacity, 2022</li>
  <li>B.E. in Information Technology, Shantilal Shah Engineering College, Bhavnagar (2019 – 2023)</li>
  <li><a href="https://ai.stackexchange.com/users/78733/keval-pandya">AI Stack Exchange</a>: <!--SE:START-->32 answers, 676 reputation<!--SE:END-->; ranked 10th by reputation on the site in 2024.</li>
  <li>Open source: <a href="https://github.com/samson-wang/cython_bbox/pull/14">samson-wang/cython_bbox#14</a>, making the package build on current NumPy.</li>
</ul>

<h2>📈 GitHub stats</h2>
<p align="center">
<img height="170" src="https://github-readme-stats.vercel.app/api?username=Keval-P&show_icons=true&hide_rank=true&hide=stars,issues&hide_border=true&bg_color=000000&title_color=DC1D47&text_color=c9d1d9&icon_color=DC1D47" alt="Keval Pandya GitHub stats" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs?username=Keval-P&layout=compact&hide_border=true&bg_color=000000&title_color=DC1D47&text_color=c9d1d9&icon_color=DC1D47" alt="Keval Pandya top languages" />
</p>

<h2>📫 Where to find me</h2>
<p align="center">
<a href="https://keval-p.github.io/"><img alt="Keval Pandya portfolio" src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&labelColor=000000&logo=githubpages&logoColor=DC1D47" /></a>
<a href="https://www.linkedin.com/in/keval-pandya-ai-ml-engineer"><img alt="Keval Pandya on LinkedIn" src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&labelColor=000000&logo=linkedin&logoColor=DC1D47" /></a>
<a href="https://ai.stackexchange.com/users/78733/keval-pandya"><img alt="Keval Pandya on AI Stack Exchange" src="https://img.shields.io/badge/AI_Stack_Exchange-000000?style=for-the-badge&labelColor=000000&logo=stackexchange&logoColor=DC1D47" /></a>
<a href="https://github.com/Keval-P"><img alt="Keval Pandya on GitHub" src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&labelColor=000000&logo=github&logoColor=DC1D47" /></a>
</p>

<p align="center"><a href="https://github.com/Keval-P/Keval-P/actions/workflows/profile.yml"><img src="https://github.com/Keval-P/Keval-P/actions/workflows/profile.yml/badge.svg" alt="Profile CI" /></a></p>
<p align="center">⏰ <!--UPDATED:START-->Updated on Thu, 19 Nov 2026<!--UPDATED:END--></p>

<p align="center"><img src="assets/footer.svg" alt="" width="100%" /></p>
