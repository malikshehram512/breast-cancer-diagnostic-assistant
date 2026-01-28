# 🏥 Breast Cancer Diagnostic Assistant

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/MalikShehram/Breast_Cancer_Diagnosis_Using_Naive_Bayes_model)
[![Docker](https://img.shields.io/badge/Docker-Enabled-0db7ed?logo=docker&logoColor=white)](https://www.docker.com/)
[![Gradio](https://img.shields.io/badge/UI-Gradio-orange)](https://gradio.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776ab?logo=python&logoColor=white)](https://www.python.org/)

An end-to-end Machine Learning pipeline that classifies breast tumor samples as **Malignant** or **Benign** using a Gaussian Naive Bayes model. Containerized with **Docker** and deployed on **Hugging Face Spaces**.

---

## 🚀 Live Demo
Access the interactive web application here:  
**[👉 Click here to view the Live Space](https://huggingface.co/spaces/MalikShehram/Breast_Cancer_Diagnosis_Using_Naive_Bayes_model)**

---

## 🔍 Project Description

The **Breast Cancer Diagnostic Assistant** is a sophisticated machine learning application designed to bridge the gap between clinical data analysis and accessible healthcare technology. At its core, the system utilizes a **Gaussian Naive Bayes (GNB) algorithm**, a probabilistic classification technique renowned for its efficiency and high performance in high-dimensional biological datasets. The model was meticulously trained on clinical data focusing on five key morphological features of cell nuclei: **mean radius, mean texture, mean perimeter, mean area, and mean smoothness.**

By calculating the conditional probability of a tumor being Malignant or Benign based on these specific features, the model provides a rapid, data-driven second opinion for diagnostic screening. The mathematical foundation relies on Bayes' Theorem:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

The integration of **Gradio** provides a high-fidelity user interface, allowing medical professionals, students, or researchers to input complex measurements via intuitive sliders and receive immediate, color-coded visual feedback. A "Malignant" prediction triggers a high-visibility red alert, while "Benign" results are displayed in calming green tones, ensuring the model’s output is both actionable and interpretable. This reduces the cognitive load required to interpret raw numerical model outputs, turning a mathematical prediction into a clear clinical insight.



[<img width="429" height="322" alt="image" src="https://github.com/user-attachments/assets/e3c435a8-d46c-4662-bd51-2369114832b4" />
]


To ensure global accessibility and cross-platform reliability, the entire environment is fully containerized using **Docker**. This approach eliminates the "it works on my machine" dilemma by bundling the Python runtime, specific library versions (such as Scikit-Learn, Joblib, and NumPy), and the application logic into a single, portable unit. Deployment on **Hugging Face Spaces** further demonstrates a modern MLOps workflow, providing a scalable, cloud-hosted platform for real-time interaction. This project highlights how simplified AI architectures, when paired with robust deployment strategies and user-centric design, can create meaningful tools for the medical field, emphasizing that accuracy in data must be matched by clarity in presentation.



---

## 🛠️ Tech Stack

* **Modeling:** Scikit-Learn (Gaussian Naive Bayes)
* **Interface:** Gradio
* **Containerization:** Docker
* **Deployment:** Hugging Face Spaces
* **Language:** Python 3.9
* **Libraries:** NumPy, Pandas, Joblib

---

## 📂 Project Structure

```text
├── app.py              # Gradio interface & prediction logic
├── model.joblib        # Trained Naive Bayes model
├── requirements.txt    # Python dependencies (pinned for stability)
├── Dockerfile          # Container configuration
└── README.md           # Project documentation
