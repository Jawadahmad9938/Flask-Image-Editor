import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import urllib.request

# Function to load image from URL

def load_image_from_url(url):
    try:
        resp = urllib.request.urlopen(url)
        image_data = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        return image
    except Exception as e:
        print(f"❌ Error loading image: {e}")
        return None


# Function for ROI selection (mouse-based)

def select_roi(image):
    clone = image.copy()
    roi = cv2.selectROI("Select ROI", clone, False, False)
    cv2.destroyWindow("Select ROI")
    if roi != (0,0,0,0):
        x, y, w, h = roi
        return (x, y, w, h)
    else:
        return None


# Function to display and adjust color channels inside ROI

def adjust_color_channels(image, roi=None):
    if image is None:
        print("❌ Error: Could not load the image.")
        return

    max_dim = 600
    h, w = image.shape[:2]
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        image = cv2.resize(image, (int(w * scale), int(h * scale)))
        print(f"📏 Image resized to: {image.shape}")

    original_image = image.copy()
    image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    plt.subplots_adjust(bottom=0.3)
    ax[0].imshow(image_rgb)
    ax[0].set_title("Original Image")
    ax[0].axis('off')

    adjusted_display = ax[1].imshow(image_rgb)
    ax[1].set_title("Adjusted Image")
    ax[1].axis('off')

    # Slider areas
    axcolor = 'lightgoldenrodyellow'
    ax_b = plt.axes([0.15, 0.18, 0.65, 0.03], facecolor=axcolor)
    ax_g = plt.axes([0.15, 0.13, 0.65, 0.03], facecolor=axcolor)
    ax_r = plt.axes([0.15, 0.08, 0.65, 0.03], facecolor=axcolor)

    slider_b = Slider(ax_b, 'Blue', -100, 100, valinit=0, valstep=1)
    slider_g = Slider(ax_g, 'Green', -100, 100, valinit=0, valstep=1)
    slider_r = Slider(ax_r, 'Red', -100, 100, valinit=0, valstep=1)

    # Reset button
    reset_ax = plt.axes([0.8, 0.02, 0.1, 0.05])
    button_reset = Button(reset_ax, 'Reset', color='lightgray', hovercolor='0.8')

    # ROI coordinates
    roi_coords = roi

    # Update function
    def update(val):
        b_offset = int(slider_b.val)
        g_offset = int(slider_g.val)
        r_offset = int(slider_r.val)

        modified = original_image.copy()

        if roi_coords:
            x, y, w, h = roi_coords
            roi_section = modified[y:y+h, x:x+w]

            b, g, r = cv2.split(roi_section)
            b = cv2.add(b, b_offset)
            g = cv2.add(g, g_offset)
            r = cv2.add(r, r_offset)

            roi_merged = cv2.merge([b, g, r])
            modified[y:y+h, x:x+w] = roi_merged
        else:
            b, g, r = cv2.split(modified)
            b = cv2.add(b, b_offset)
            g = cv2.add(g, g_offset)
            r = cv2.add(r, r_offset)
            modified = cv2.merge([b, g, r])

        rgb_merged = cv2.cvtColor(modified, cv2.COLOR_BGR2RGB)
        adjusted_display.set_data(rgb_merged)
        fig.canvas.draw_idle()

    # Reset function
    def reset(event):
        slider_b.reset()
        slider_g.reset()
        slider_r.reset()

    slider_b.on_changed(update)
    slider_g.on_changed(update)
    slider_r.on_changed(update)
    button_reset.on_clicked(reset)

    plt.show()


# --------------------------
# Main Execution
# --------------------------
if __name__ == "__main__":
    print("🔗 Enter an image URL (e.g., https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d):")
    image_url = input("Image URL: ").strip()

    if not image_url:
        print("❌ No URL provided. Exiting.")
    else:
        image = load_image_from_url(image_url)

        # Let user select ROI
        print("🎯 Select ROI (drag rectangle on image window)...")
        roi = select_roi(image)

        if roi:
            print(f"✅ ROI selected: {roi}")
        else:
            print("⚠️ No ROI selected, applying to full image.")

        adjust_color_channels(image, roi)
