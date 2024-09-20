## 🚀 Async Experiment with FastAPI

### 🌟 Overview

This project showcases a **FastAPI** application that compares **blocking** and **non-blocking** API calls, highlighting how **asynchronous programming** can significantly enhance performance in web applications. 🌐✨

### 📂 Project Structure

- **benchmark_requests.py**: Script for benchmarking API calls. 📊
- **requirements.txt**: Lists project dependencies. 📜
- **src/**: Contains application files. 📁
  - **app.py**: Defines the FastAPI application with endpoints. ⚙️
  - **__init__.py**: Initializes the package. 📦

### 🔑 Key Components

- **Blocking Calls**: Simple but can slow down response times ⏳ and are not efficient for multiple simultaneous requests. ❌
- **Non-Blocking Calls**: More efficient and scalable 🚀, allowing multiple requests to be handled while waiting for responses. ✔️

### 🚀 Getting Started

#### ✅ Requirements

- Python 3.7 or higher 🐍
- Virtual environment , isolate your experiments is highly recomended !🌿

#### 🔧 Installation Steps

1. Clone the repository, navigate to the project directory. 🖥️
2. Set up a virtual env `python -m venv .venv`. 🌱
3. Install the necessary dependencies listed in `requirements.txt`. 📥

#### 📈 Running the Benchmark

Run the benchmarking script to see the performance comparison between blocking and non-blocking calls. 🏃‍♂️💨
Results : 

Time taken to make 1000 requests to blocking-fetch endpoint: 148.55562615394592 seconds
Time taken to make 1000 requests to non-blocking-fetch endpoint: 160.3681812286377 seconds requirements.txt 