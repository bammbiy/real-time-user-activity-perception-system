# Real-Time User Activity Perception System

A production-oriented computer vision system that detects, tracks, and classifies user activities (gaming, webtoon reading, idle) in real time using detection, multi-object tracking, and temporal deep learning.

---

## 🚀 Overview

This project simulates a real-world AI service pipeline focused on real-time perception, scalable inference, and system-level design.

The system processes live video input and performs:

- Object Detection (user presence)
- Multi-Object Tracking (ID consistency across frames)
- Temporal Activity Classification
- Real-time inference via API

Unlike typical ML demos, this project emphasizes **end-to-end system design**, including frontend, backend, AI pipeline, and deployment structure.

---

## 🧠 Key Features

- Real-time activity recognition pipeline
- Multi-object tracking with ID consistency
- Temporal modeling using sequence-based learning
- Modular AI pipeline (Detection → Tracking → Classification)
- FastAPI-based backend inference server
- React-based frontend for live interaction
- Container-ready architecture (Docker / Kubernetes ready)
- Extendable to Triton Inference Server for scalable deployment

---

## 🏗️ System Architecture

Frontend (React)  
→ FastAPI Backend  
→ AI Pipeline  
  ├── Detection (YOLO)  
  ├── Tracking (IoU-based Tracker)  
  └── Activity Classification (Temporal CNN)  
→ Inference Output  

---

## 📂 Project Structure

.
├── frontend/        # React client (video capture & API request)  
├── backend/         # FastAPI server (inference API)  
├── ai_core/         # Core ML pipeline  
│   ├── detection/  
│   ├── tracking/  
│   ├── activity/  
│   └── pipeline/  
├── infra/           # Docker / Kubernetes configs  
├── dataset/         # Sequence dataset (training data)  
└── scripts/         # data processing / training / export  

---

## ⚙️ Tech Stack

Backend:
- FastAPI
- Python

Frontend:
- React (TypeScript)
- Axios

AI / ML:
- PyTorch
- OpenCV

Model Components:
- Detection: YOLO
- Tracking: IoU-based tracker (extendable to ByteTrack / DeepSORT)
- Classification: Temporal CNN

Deployment:
- Docker
- Kubernetes
- Triton Inference Server (designed for integration)

---

## 🧪 Machine Learning Approach

### Problem Definition

Classify user activity into:
- Gaming
- Webtoon Reading
- Idle

---

### Pipeline

1. Capture video stream  
2. Extract frames  
3. Detect objects (bounding boxes)  
4. Track objects across frames (ID consistency)  
5. Generate temporal sequences  
6. Perform activity classification using temporal model  

---

### Model Design

- Temporal CNN (sequence-based classification)
- Input: sequence of bounding box features over time
- Output: activity class (3 classes)

---

## 📊 Dataset Strategy

Instead of single images, this project uses **sequence-based data**:

Each sample consists of multiple consecutive frames:

{
  "sequence": [
    {"bbox": [x1, y1, x2, y2]},
    ...
  ],
  "label": "GAMING"
}

This enables temporal modeling of user behavior.

---

## 🧠 Training Pipeline

- Frame extraction from raw videos
- Detection + tracking to generate structured data
- Sequence generation (sliding window)
- PyTorch dataset loader
- Model training using cross-entropy loss
- ONNX export for deployment

---

## 🔄 Semi-Supervised Learning (Advanced)

To address limited labeled data:

- Pseudo-labeling applied to unlabeled sequences
- Confidence threshold filtering
- Iterative training with expanded dataset

This improves generalization without requiring full manual annotation.

---

## 🧍‍♂️ Pose & 3D Extension

- Pose estimation (MediaPipe) used for additional features
- 3D pose (x, y, z) structure prepared
- Depth estimation module included (extendable to MiDaS)

This enables future expansion toward **3D scene understanding**.

---

## 📊 Challenges & Solutions

### Temporal Dependency
- Problem: Single-frame classification is unreliable  
- Solution: Sequence-based temporal modeling  

### Identity Consistency
- Problem: Detection alone loses identity  
- Solution: Tracking with ID persistence  

### Data Scarcity
- Problem: Limited labeled sequences  
- Solution: Semi-supervised learning (pseudo labeling)  

### Real-Time Constraint
- Problem: Latency vs accuracy trade-off  
- Solution: Lightweight modular pipeline  

---

## 📉 Limitations

- Tracking may degrade under occlusion
- Detection performance drops in low-light environments
- Current tracker is simplified (IoU-based)
- Activity model performance depends on sequence quality

---

## 🔧 Future Improvements

- Replace tracker with ByteTrack or DeepSORT
- Integrate Triton Inference Server for production inference
- Improve temporal model (LSTM / Transformer)
- Add pose-based feature fusion
- Apply full 3D scene understanding (depth + pose)
- Optimize latency for edge deployment

---

## ▶️ How to Run

### Backend

cd backend  
uvicorn app.main:app --reload  

---

### Frontend

cd frontend  
npm install  
npm start  

---

## 🎯 Key Takeaways

This project demonstrates:

- End-to-end AI system design
- Real-time computer vision pipeline
- Temporal modeling for behavior analysis
- Practical deployment considerations
- Clear separation of frontend, backend, and AI modules

---

## 📌 Author Note

This project focuses on **system-level design and real-world deployment considerations**, rather than isolated model performance.

It is designed to reflect how computer vision systems are built and deployed in production environments.

---
