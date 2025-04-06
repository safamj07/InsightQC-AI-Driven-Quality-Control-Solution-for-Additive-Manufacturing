# 📊 Results and Discussions

The performance evaluation of **InsightQC** demonstrates its effectiveness in real-time defect detection and automated quality control.

Traditional systems such as manual inspections and conventional machine vision methods have long served the industry but are inefficient, slow, and prone to human error. In contrast, **InsightQC** integrates deep learning (YOLOv8) with Robotic Process Automation (RPA), enabling a fully automated and intelligent defect detection system to enhance manufacturing efficiency and reduce costs.
---

## 5.1 📌 Comparison with Traditional and Existing Systems

| Feature/Model | Traditional Vision-Based Models | ML-Based Models (e.g., VGG16, CNNs) | Multimodal Sensor Fusion Models | **InsightQC (Proposed System)** |
|--------------|-------------------------------|-----------------------------------|-------------------------------|-------------------------------|
| **Defect Detection Accuracy** | ~75-85% | ~85-92% | ~92-98% | **95-99%** (Optimized YOLOv8) |
| **Real-Time Processing** | Slower, batch-based | Depends on model | Faster, requires sensors | **High-speed YOLOv8 real-time** |
| **Automation & Integration** | Manual review | Lacks automation | Complex to automate | **Integrated with RPA** |
| **Sensor Integration** | Only visual | Mostly image-based | Visual + Thermal + Acoustic | **Flexible sensor fusion** |
| **Scalability & Adaptability** | Not adaptive | Requires retraining | Limited flexibility | **Dynamic learning model** |
| **Cost & Hardware** | Low cost | Medium (GPU, ML expertise) | High cost (special sensors) | **Cloud-based, scalable** |
| **Maintenance & Reporting** | Manual only | Limited reporting | Semi-automated | **Fully automated with scheduling** |

> 📌 **Table 5.1**: InsightQC vs Existing Systems

---

## 5.2 📐 Performance Metrics and Formulas (YOLOv8 + RPA)

The model was tested using **1,000 images** including various defects (cracks, porosity, misalignment, etc.).

### ✅ Achieved Metrics:
- **mAP@50-95**: 85%
- **Precision**: 87%
- **Recall**: 89%
- **Inference Speed**: 30ms/image (Real-time)

![WhatsApp Image 2024-04-29 at 7 29 54 PM - Copy](https://github.com/user-attachments/assets/0ddc8a97-02f9-48e4-b15d-7c4ca0ed69ba)

![Screenshot 2025-02-09 212235](https://github.com/user-attachments/assets/a70efa60-2065-46db-8af3-bbfbbcd49c1b)

### 📏 Key Formulas:

```text
Accuracy       = (TP + TN) / (TP + TN + FP + FN)
Precision      = TP / (TP + FP)
Recall         = TP / (TP + FN)
F1 Score       = 2 * (Precision * Recall) / (Precision + Recall)
mAP            = (1/N) * ∑(AP_i)
IoU            = Area of Overlap / Area of Union
Inference Time = Total Time / Number of Images
Defect Reduction Rate = ((Defects_Before - Defects_After) / Defects_Before) * 100

