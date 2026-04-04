# AI-Powered KYC System – Face Verification Module

## Project Overview
This repository contains the Face Verification module of the AI-Powered Identity Verification & Fraud Detection system for KYC compliance.

The goal of this module is to verify whether a live selfie matches the official ID photo using deep learning-based facial embeddings.

---

## Contribution

• Designed complete preprocessing pipeline  
• Implemented face detection using MTCNN (with Haar fallback)  
• Implemented face cropping and alignment  
• Applied normalization and contrast enhancement  
• Added training data augmentation  
• Structured train / validation / test splits  
• Integrated FaceNet for embedding generation  
• Implemented cosine similarity-based verification  
• Evaluated model using accuracy and confusion matrix  

---

## Pipeline Overview

1. Dataset scanning and pairing
2. Train/Validation/Test split
3. Face detection
4. Face cropping
5. Face alignment
6. Normalization (224x224, float32 [0,1])
7. Data augmentation (train only)
8. FaceNet embedding extraction (512-d)
9. Cosine similarity matching
10. Threshold-based verification

---
## Flow Of Preprocessing








## Model Details

Embedding Model: FaceNet  
Embedding Size: 512  
Similarity Metric: Cosine Similarity  
Decision Rule: Similarity > Threshold → Match  

---

## Evaluation Metrics

• Accuracy  
• Confusion Matrix  
• Preprocessing success rate  

---

## Output Structure

Processed images saved as `.npy` files:
train/
val/
test/

Metadata saved as CSV files.

---

## Future Improvements

• Larger dataset evaluation  
• Threshold optimization  
• ROC curve analysis  
• Liveness detection integration  
• Bias and fairness evaluation  

---

## Team Project Context

This module is part of the larger AI-powered KYC system which also includes:

• Document verification  
• OCR  
• Tampering detection  
• Fraud risk scoring  
• Human-in-the-loop validation  

---
## 📜 Copyright

© 2026 Vidzai Digital Private Limited. All rights reserved.

Author: Deeksha H L  
Role: Face Verification & Preprocessing
