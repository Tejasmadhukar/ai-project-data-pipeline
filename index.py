import os
import csv
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CSV_FILE = "videos.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["youtube_id"])

OUTPUT_DIR = "downloaded_comments"
if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

def download_comments(video_id):
    output_file = os.path.join(OUTPUT_DIR, f"{video_id}.json")
    subprocess.run(["./script.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


@app.route('/')
def home():
    return 'Api is Healthy'


@app.route("/add_video", methods=["POST"])
def add_video():    
    data = request.get_json()
    if "youtube_id" not in data:
        return jsonify({"error": "Missing 'youtube_id' in request body"}), 400

    youtube_id = data["youtube_id"]

    # Check if the CSV file is empty or doesn't exist
    if not os.path.exists(CSV_FILE) or os.stat(CSV_FILE).st_size == 0:
        with open(CSV_FILE, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["youtube_id"])

    # Add the video ID to the CSV
    with open(CSV_FILE, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([youtube_id])

    # Download comments for the video
    download_comments(youtube_id)

    return jsonify({"message": "Video added to CSV and comments downloaded successfully"})

if __name__ == "__main__":
    p = int(os.getenv('PORT', 80))
    app.run(host='0.0.0.0', port=p)