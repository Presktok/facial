# 🔐 FaceAuth – Facial Recognition Authentication System

<p align="center">
  <b>A secure facial authentication system built with Flask & OpenCV</b><br>
  🧠 Computer Vision • 🔒 Cybersecurity • 🌐 Web Application
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask">
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-green">
  <img src="https://img.shields.io/badge/Status-Active-success">
</p>

---

## 🚀 Overview

**FaceAuth** is a secure and scalable **facial recognition–based authentication system** designed to eliminate traditional passwords. Built using **Flask**, **OpenCV**, and computer vision techniques, it enables real-time user authentication through a clean and intuitive web interface.

This project is ideal for **secure access control**, academic demonstrations, and cybersecurity-focused applications.

---

## ✨ Features

✔️ User registration with multiple facial image captures  
✔️ Real-time facial recognition via webcam  
✔️ Secure session-based authentication  
✔️ User dashboard access control  
✔️ Automatic model retraining on user add/delete  
✔️ User management (view & delete users)  
✔️ Robust error handling  

---

## 🛡️ Security Highlights

- Password-less biometric authentication  
- Flask session-based access control  
- Automatic retraining prevents stale identities  
- Controlled dataset storage per user  

---

## 🖼️ Screenshots

| Homepage | Registration | Recognition |
|--------|--------------|-------------|
| ![Homepage](https://github.com/user-attachments/assets/1dad9fef-bea4-4531-b443-5f6f371bc3a0) | ![Registration](https://github.com/user-attachments/assets/cbd706f3-a904-4faf-b5c3-a7a2e2db8b45) | ![Recognition](https://github.com/user-attachments/assets/2bc273e5-0d54-42eb-9392-df1435a17bf5) |

---

## 🧠 Tech Stack

- **Backend:** Flask (Python)
- **Computer Vision:** OpenCV
- **ML Algorithm:** LBPH Face Recognizer
- **Frontend:** HTML, CSS, Jinja Templates
- **Session Management:** Flask Sessions
- **Storage:** File-based dataset

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-url>
cd facial
2️⃣ Create & Activate Virtual Environment
python -m venv venv

Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install Flask opencv-python numpy

If OpenCV causes issues:
pip install opencv-python-headless

▶️ Run the Application
python app.py

🌐 Open in browser:
👉 http://localhost:5000

📘 Usage Guide
🔹 Register New User
Visit /register

Enter a unique username
Start face scan and align your face
System captures images and trains the model

🔹 Recognize User
Go to /recognize
Start recognition
On success, redirected to dashboard

🔹 Delete User
Open registration page
Select and delete user
Model retrains automatically

## Important Notes - Prefer localhost:5000 over 127.0.0.1:5000 for camera access - Ensure your webcam is properly connected - Use Chrome or Firefox for best compatibility
