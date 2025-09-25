# 🎨 Flask Image Editor

A lightweight Flask-based web app for editing images directly in the browser.  
Users can upload an image, adjust RGB channels in real-time with sliders, select ROI (Region of Interest), and save the final result.

---

## ✨ Features
- 📤 Upload any image (JPG, PNG, etc.)
- 🎛 Adjust **Red, Green, Blue** channels with live preview
- 🎯 ROI (Region of Interest) editing support
- 💾 Save adjusted image instantly
- ⚡ Built using **Flask + OpenCV + JavaScript**

---

## 📂 Project Structure
Flask-Image-Editor/
│── static/
│ ├── uploads/ # uploaded + processed images
│ └── style.css # frontend styling
│── templates/
│ ├── index.html # upload page
│ └── editor.html # editor page with sliders
│── app.py # main Flask app
│── README.md # project documentation


---

## 🚀 Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/Flask-Image-Editor.git
cd Flask-Image-Editor

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install flask opencv-python numpy

4️⃣ Run the app
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000


🖼️ Demo Workflow

Upload an image

Use sliders to adjust Blue / Green / Red channels

ROI selection (optional)

Save the adjusted image

🛠️ Tech Stack

Backend: Flask (Python)

Image Processing: OpenCV, NumPy

Frontend: HTML, CSS, JavaScript (fetch API)

📜 License

MIT License © 2025

🤝 Contributing

PRs are welcome!
If you have ideas for features like filters, brightness/contrast control, or crop tools — feel free to fork and improve 🚀
