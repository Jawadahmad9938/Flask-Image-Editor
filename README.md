# 🎨 Flask Image Editor

A lightweight Flask-based web application for real-time image editing directly in your browser. Upload images, adjust RGB channels with intuitive sliders, select specific regions for editing, and save your masterpiece with ease.

![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)

## ✨ Features

- 📤 **Easy Upload** - Support for JPG, PNG, and other common image formats
- 🎛 **Real-time RGB Adjustment** - Interactive sliders for precise color control
- 🎯 **ROI Editing** - Select specific regions for targeted adjustments
- 💾 **Instant Save** - Download your edited images immediately
- ⚡ **Fast Processing** - Powered by Flask + OpenCV + JavaScript
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices

## 📸 Demo

![Demo GIF](https://via.placeholder.com/800x400.png?text=Flask+Image+Editor+Demo)

## 📂 Project Structure

```
Flask-Image-Editor/
│
├── static/
│   ├── uploads/                 # Directory for uploaded and processed images
│   ├── css/
│   │   └── style.css            # Frontend styling and responsive design
│   └── js/
│       └── script.js            # Client-side JavaScript functionality
│
├── templates/
│   ├── base.html                # Base template with common elements
│   ├── index.html               # Image upload page
│   └── editor.html              # Editor interface with sliders and preview
│
├── app.py                       # Main Flask application
├── image_processor.py           # Image processing utilities
├── requirements.txt             # Project dependencies
├── config.py                    # Configuration settings
└── README.md                    # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Flask-Image-Editor.git
   cd Flask-Image-Editor
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser and navigate to**
   ```
   http://127.0.0.1:5000
   ```

## 🛠️ Usage Guide

### Basic Workflow

1. **Upload Image**
   - Click "Choose File" to select an image from your device
   - Supported formats: JPG, PNG, BMP, WebP
   - Maximum file size: 16MB

2. **Edit Image**
   - Use the Red, Green, and Blue sliders to adjust color channels
   - Real-time preview updates as you make changes
   - Select ROI (Region of Interest) for targeted editing
   - Reset button reverts all changes

3. **Save Result**
   - Click "Save Image" to download the edited version
   - Images are saved in their original format

### Advanced Features

- **ROI Selection**: Click and drag on the image to select a specific region for editing
- **Preset Filters**: Apply predefined color filters (coming soon)
- **Batch Processing**: Edit multiple images sequentially (coming soon)

## 🔧 Configuration

Edit `config.py` to customize application settings:

```python
class Config:
    # File upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.webp']
    
    # Image processing settings
    DEFAULT_QUALITY = 95
    MAX_DIMENSION = 4000  # Maximum width/height for processed images
```

## 🧩 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Render upload page |
| POST | `/upload` | Handle image upload |
| GET | `/editor/<filename>` | Render editor with uploaded image |
| POST | `/adjust` | Process image adjustments |
| GET | `/download/<filename>` | Download edited image |

## 🐛 Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'flask'"**
   - Solution: Ensure all dependencies are installed: `pip install -r requirements.txt`

2. **"413 Request Entity Too Large"**
   - Solution: The uploaded image exceeds the size limit (16MB)

3. **Image not loading in editor**
   - Solution: Check browser console for errors and ensure image format is supported

4. **Sliders not working**
   - Solution: Ensure JavaScript is enabled in your browser

### Debug Mode

Enable debug mode for detailed error messages:
```python
app.run(debug=True)
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Feature Requests
- ✨ Brightness/Contrast controls
- 🎨 Filter presets (vintage, black & white, etc.)
- ✂️ Crop and rotate tools
- 🔄 Batch processing mode
- 📊 Histogram display

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Image processing powered by [OpenCV](https://opencv.org/)
- UI components inspired by modern web design principles

## 📞 Support

- 📧 Email: jawadahmad9938@gmail.com
- 🐛 [Issue Tracker](https://github.com/your-username/Flask-Image-Editor/issues)
- 💬 [Discussions](https://github.com/your-username/Flask-Image-Editor/discussions)


<div align="center">

⭐ **Don't forget to star this repo if you find it useful!**

</div>