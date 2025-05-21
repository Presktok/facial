from flask import Flask, request, jsonify, render_template
import os
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html', active_tab='register')

@app.route('/recognize')
def recognize():
    return render_template('recognize.html', active_tab='recognize')

@app.route('/upload-face', methods=['POST'])
def upload_face():
    username = request.args.get('username')
    count = request.args.get('count')
    image_data = request.get_json()['image']

    image_data = image_data.split(',')[1]  # Remove the base64 header
    image_data = base64.b64decode(image_data)

    user_dir = f"dataset/{username}"
    os.makedirs(user_dir, exist_ok=True)

    image_path = f"{user_dir}/{count}.jpg"
    with open(image_path, 'wb') as f:
        f.write(image_data)

    return jsonify({"status": "success", "message": "Image saved."})

@app.route('/train', methods=['POST'])
def train_model():
    try:
        # Stub for training logic
        print("Training model...")
        return jsonify({"status": "success", "message": "Training completed."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/start-recognition')
def start_recognition():
    try:
        # Stub for recognition logic
        result = "✅ User recognized: johndoe"
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
