Here’s a reorganized and formatted version of your README.md for the FaceAuth project. The structure is clarified, sections are streamlined, and instructions are made more concise for easier readability.

---

# FaceAuth - Facial Recognition System

## Overview

FaceAuth is a robust facial authentication system built with **Flask**, **OpenCV**, and deep learning techniques. It delivers seamless and secure access control for various applications, enabling user registration, facial recognition, and user management through an intuitive web interface.

---

## Features

- **User Registration:** Register new users by capturing multiple facial images.
- **Facial Recognition:** Authenticate users by comparing live camera feeds with registered data.
- **User Management:** View and delete registered users.
- **Model Training:** Automatically retrains when users are added or deleted.
- **Secure Sessions:** Uses Flask sessions for secure logins and dashboard access.
- **Error Handling:** Robust handling for camera, model, and file errors.

---

## Screenshots

| Homepage                                       | Registration Page                                 | Recognition Page                                   |
|------------------------------------------------|---------------------------------------------------|----------------------------------------------------|
| ![Homepage](![Screenshot 2025-06-08 180629](https://github.com/user-attachments/assets/1dad9fef-bea4-4531-b443-5f6f371bc3a0)
)               | ![Registration](images/registration_page.png)     | ![Recognition](images/recognition_page.png)        |

---

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone <your-repository-url>
    cd facial
    ```
2. **Create and activate a virtual environment**
    - Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - macOS/Linux:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
3. **Install dependencies**
    ```bash
    pip install Flask opencv-python numpy
    ```
    > If you have issues with `opencv-python`, try `pip install opencv-python-headless`.
4. **Place pre-trained models**
    - Ensure `haarcascade_frontalface_default.xml` (from OpenCV) is available and accessible by your script. Usually, `cv2.data.haarcascades` points to it.

---

## Running the Application

1. **Activate your virtual environment** (if not already active)
2. **Start the Flask app**
    ```bash
    python app.py
    ```
3. **Access the application**
    - Go to [http://localhost:5000](http://localhost:5000) in your web browser.

---

## Usage Guide

### 1. Register a New User
- Navigate to `/register`
- Enter a unique username
- Click “Start Face Scan” and center your face in the camera feed
- When enough images are captured, the system will train and confirm registration

### 2. Recognize a User
- Go to `/recognize`
- Click “Start Recognition”
- If recognized, you’ll be redirected to your dashboard

### 3. Delete a User
- On the `/register` page, view the user list
- Click “Delete” to remove a user
- The model retrains or deletes files if no users remain

---

## Project Structure

```
facial/
├── app.py                 # Main Flask app
├── recognize.py           # Face recognition logic
├── templates/             # Web HTML templates
│   ├── index.html
│   ├── register.html
│   ├── recognize.html
│   └── dashboard.html
├── dataset/               # Captured images for each user
│   └── <username>/
│       ├── 1.jpg
│       └── ...
├── trained_model/         # Recognition model and labels
│   ├── trainer.yml
│   └── labels.txt
├── images/                # Screenshots/documentation images
│   ├── homepage.png
│   ├── registration_page.png
│   └── recognition_page.png
└── README.md
```

---

## Important Notes

- Prefer `localhost:5000` over `127.0.0.1:5000` for camera access
- Ensure your webcam is properly connected
- Use Chrome or Firefox for best compatibility

---

If you’d like further customization or additional sections, let me know!
