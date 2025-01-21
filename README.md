# Dataset Preparation CarDD

1. **Download the Dataset CarDD_release**  
   Download the dataset from the following Google Drive link:  
   [Dataset Link](https://drive.google.com/file/d/1bbyqVCKZX5Ur5Zg-uKj0jD0maWAVeOLx/view)

2. **Place the Dataset**  
   After downloading, place the dataset at the same directory level as the `data_prep.ipynb` file.
   ![](https://github.com/rogerhsiehh/ADA-Project/blob/6232998f1e5cb24e30bda3853722220ab8200879/info/Screenshot%202024-12-23%20at%2011.20.51.png)

3. **Run the Code**  
   Open and execute the `data_prep.ipynb` notebook. Once completed, you will receive the processed data label vectors for all train, test, and validation files.

---
# Dataset Preparation Kaggle Car Damage Severity

1. **Download the Dataset Car Damage Severity**  
   Download the dataset from the following link:  
   [Dataset Link](https://www.kaggle.com/datasets/prajwalbhamere/car-damage-severity-dataset/data)

2. **Run the Code**  
   Data Pre-processing and Models are in the same files.

# Models

1. **YOLO**

- **Availabe Pre-trained Detection Models**:
   - ([https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)). 

3. **ViT**

- Vision Transformers (ViT) are state-of-the-art models for image classification, utilizing transformer architecture to capture global context.

- **Available Pre-trained Models**:
  - [ViT-Base (Patch 16, 224px)](https://huggingface.co/google/vit-base-patch16-224-in21k)  
    Pre-trained on ImageNet-21k and fine-tuned for image classification.
  - [ViT-Large (Patch 32, 384px)](https://huggingface.co/google/vit-large-patch32-384)  
    A larger ViT model for high-resolution tasks.
  - [ViT-Huge (Patch 14, 224px)](https://huggingface.co/google/vit-huge-patch14-224-in21k)  
    A high-capacity ViT model for tasks requiring deep learning power.

---
