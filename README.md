# Face Recognition System

A web-based face recognition system built with Flask and OpenCV.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Access the application:
Open your browser and go to: http://localhost:5000

## Usage

1. Registration:
   - Click on the "Register" tab
   - Enter your name
   - Allow camera access when prompted
   - Click "Start Face Scan"
   - Move your head slightly between captures
   - Wait for the training to complete

2. Recognition:
   - Click on the "Recognize" tab
   - Click "Start Recognition"
   - The system will identify registered faces

## Project Structure

```
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   ├── register.html   # Registration page
│   ├── recognize.html  # Recognition page
│   └── dashboard.html  # Dashboard after successful recognition
├── dataset/           # Stored face images
├── trained_model/     # Trained model files
├── requirements.txt   # Project dependencies
└── README.md         # This file
```

## Important Notes

- Always use `localhost:5000` instead of `127.0.0.1:5000` for camera access
- Make sure your webcam is properly connected and accessible
- Use Chrome or Firefox for best compatibility 