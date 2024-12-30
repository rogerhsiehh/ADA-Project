# Dataset Preparation

1. **Download the Dataset CarDD_release**  
   Download the dataset from the following Google Drive link:  
   [Dataset Link](https://drive.google.com/file/d/1bbyqVCKZX5Ur5Zg-uKj0jD0maWAVeOLx/view)

2. **Place the Dataset**  
   After downloading, place the dataset at the same directory level as the `data_prep.ipynb` file.
   ![](https://github.com/rogerhsiehh/ADA-Project/blob/6232998f1e5cb24e30bda3853722220ab8200879/info/Screenshot%202024-12-23%20at%2011.20.51.png)

4. **Run the Code**  
   Open and execute the `data_prep.ipynb` notebook. Once completed, you will receive the processed data label vectors for all train, test, and validation files.

---


# Pre-trained Models Available on Hugging Face

This project leverages pre-trained models from Hugging Face for efficient transfer learning. Below is a list of recommended pre-trained models that you can use, along with their descriptions and links.

---

## **1. VGG Models**
VGG models are popular for image classification tasks due to their simple architecture and strong performance on ImageNet.

- **Available Pre-trained Models**:
  - [VGG11 on ImageNet](https://huggingface.co/timm/vgg11.tv_in1k)  
    A lightweight VGG model with 11 layers.
  - [VGG19 on ImageNet](https://huggingface.co/keras/vgg_19_imagenet)  
    A deeper variant of VGG with 19 layers, pre-trained on ImageNet.

---

## **2. ResNet Models**
ResNet models are known for their residual connections, which allow for deeper architectures and high accuracy.

- **Available Pre-trained Models**:
  - [ResNet50 on ImageNet](https://huggingface.co/timm/resnet50.tv_in1k)  
    A 50-layer ResNet, widely used for classification tasks.
  - [ResNet101 on ImageNet](https://huggingface.co/timm/resnet101.tv_in1k)  
    A deeper ResNet model with 101 layers.
  - [ResNet152 on ImageNet](https://huggingface.co/timm/resnet152.tv_in1k)  
    A high-capacity ResNet model for complex tasks.

---

## **3. Vision Transformer (ViT) Models**
Vision Transformers (ViT) are state-of-the-art models for image classification, utilizing transformer architecture to capture global context.

- **Available Pre-trained Models**:
  - [ViT-Base (Patch 16, 224px)](https://huggingface.co/google/vit-base-patch16-224-in21k)  
    Pre-trained on ImageNet-21k and fine-tuned for image classification.
  - [ViT-Large (Patch 32, 384px)](https://huggingface.co/google/vit-large-patch32-384)  
    A larger ViT model for high-resolution tasks.
  - [ViT-Huge (Patch 14, 224px)](https://huggingface.co/google/vit-huge-patch14-224-in21k)  
    A high-capacity ViT model for tasks requiring deep learning power.

---
