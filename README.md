# Viral Rash Classification
![alt text](image-classification/images/rash_image.png)

![alt text](image-classification/images/ml_visualization.gif)

## Project Overview
This project aims to classify three infectious skin diseases - Chickenpox, Measles, and Monkeypox - using various deep learning models. The goal is to compare the performance of different architectures on a relatively small dataset of medical images.


### 1. Cloning the Repository

Clone the repository using the following command:

```bash
git clone https://github.com/enggabhishek/viral-rash-classification.git
```

### 2. Setting up a Virtual Environment

#### Windows

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

#### macOS/Linux

```bash
# Create a virtual environment
python3.11 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### 3. Installing Requirements

Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### Dataset

<b>Total classes</b>: 3 (Chickenpox, Measles, Monkeypox) </br>
<b>Training data</b>: 160 images per class (480 total)</br>
<b>Validation data</b>: 33 images per class (99 total)</br>

## Models Implemented

### Custom CNN

<b>Parameters</b>: 31.58 million</br>
<b>Architecture</b>: Custom-designed convolutional neural network</br>


### ResNet50

<b>Parameters</b>: 23 million (pretrained)</br>
<b>Architecture</b>: 50-layer residual network</br>


### Inception-ResNet-V2

<b>Parameters</b>: 55.9 million (pretrained)</br>
<b>Architecture</b>: Hybrid of Inception and ResNet architectures</br>


### NASNet-A-Large

<b>Parameters</b>: 89 million (pretrained)</br>
<b>Architecture</b>: Neural Architecture Search Network</br>

## YOLO11n Classification

<p>YOLO11 classification is an evolution of the YOLO (You Only Look Once) architecture tailored for image classification tasks. It processes images in real-time, leveraging its speed and accuracy.</p>

![alt text](image-classification/images/yolo_true_pred.png)

Download images folder from the following link:
<a href ='https://drive.google.com/file/d/1uRUF5hoAjwKuinrVuZV49FSMaXhrOHlZ/view?usp=sharing'> Rash Images</a>