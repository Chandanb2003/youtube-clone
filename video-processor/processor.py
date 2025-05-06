from flask import Flask, request
import os
import subprocess

app = Flask(__name__)
UPLOAD_DIR = 'uploads'
PROCESSED_DIR = 'processed'

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

@app.route('/process', methods=['POST'])
def process_video():
    file = request.files['video']
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    processed_path = os.path.join(PROCESSED_DIR, f"processed_{file.filename}")

    file.save(file_path)

    # Simulate processing using FFmpeg (e.g., re-encode to MP4)
    subprocess.call(['ffmpeg', '-i', file_path, '-vcodec', 'libx264', processed_path])

    return f"Processed video saved to {processed_path}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
