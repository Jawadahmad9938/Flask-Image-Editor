from flask import Flask, render_template, request, jsonify, url_for
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

original_image = None
current_filename = None
last_adjusted_path = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    global original_image, current_filename, last_adjusted_path

    file = request.files.get("image")
    if not file or file.filename == "":
        return "❌ No file uploaded", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    original_image = cv2.imread(filepath)
    current_filename = filename
    last_adjusted_path = filepath  

    return render_template("editor.html", filename=filename)


@app.route("/adjust", methods=["POST"])
def adjust_image():
    global original_image, current_filename, last_adjusted_path

    if original_image is None:
        return jsonify({"error": "No image uploaded"}), 400

    data = request.json
    blue = int(data.get("blue", 0))
    green = int(data.get("green", 0))
    red = int(data.get("red", 0))
    roi = data.get("roi", None) 

    modified = original_image.copy()

    if roi:
        x, y, w, h = map(int, roi)
        roi_section = modified[y:y+h, x:x+w]
        b, g, r = cv2.split(roi_section)
        b = cv2.add(b, blue)
        g = cv2.add(g, green)
        r = cv2.add(r, red)
        roi_merged = cv2.merge([b, g, r])
        modified[y:y+h, x:x+w] = roi_merged
    else:
        b, g, r = cv2.split(modified)
        b = cv2.add(b, blue)
        g = cv2.add(g, green)
        r = cv2.add(r, red)
        modified = cv2.merge([b, g, r])

    adjusted_name = "adjusted_" + current_filename
    adjusted_path = os.path.join(app.config["UPLOAD_FOLDER"], adjusted_name)
    cv2.imwrite(adjusted_path, modified)

    last_adjusted_path = adjusted_path

    return jsonify({"adjusted_url": url_for("static", filename=f"uploads/{adjusted_name}")})


@app.route("/save", methods=["POST"])
def save_image():
    global last_adjusted_path

    if not last_adjusted_path or not os.path.exists(last_adjusted_path):
        return jsonify({"error": "No adjusted image found"}), 400

    saved_name = "saved_image.png"
    saved_path = os.path.join(app.config["UPLOAD_FOLDER"], saved_name)

    shutil.copy(last_adjusted_path, saved_path)

    return jsonify({"saved_url": url_for("static", filename=f"uploads/{saved_name}")})


if __name__ == "__main__":
    app.run(debug=True)
