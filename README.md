# Digital Image Processing - Assignment #02
This digital image processing assignment includes different image processing techniques like edge detection, color segmentation, histogram equalization, adaptive thresholding, and object measurement.

## 📁 Directory Structure

```
.
├── main.py              # Script containing all Q1–Q7 functions
├── data/                # Folder containing input images
│   ├── squares.tif
│   ├── road.jpg
│   ├── hexagon.jpg
│   ├── hexagon2.jpg
│   ├── fundus.jpg
│   ├── text1.tif
│   ├── text2.tif
```

---

## ⚙️ Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib (optional, for histogram plotting)

Install dependencies using:

```bash
pip install opencv-python numpy matplotlib
```

---

## 🚀 How to Run

Run the script from your terminal:

```bash
python main.py
```

To test specific questions, uncomment the relevant function call at the bottom of `main.py`.

---

## 🔍 Function Descriptions

### `q1()` – Laplacian and Canny Edge Detection

- Applies Laplacian and Canny filters to detect edges in `squares.tif`.
- Visualizes how different methods highlight edges.

---

### `q2()` – Blue Object Segmentation

- Detects blue regions (e.g. road sign) in `road.jpg`.
- Converts to HSV, thresholds blue, and filters large contours.

---

### `q3()` – Line Detection via Custom Kernels

- Applies directional edge detection on `hexagon.jpg`.
- Uses custom kernels for horizontal, vertical, and diagonal lines.
- Visualizes with helper function `findLines()`.

---

### `q4()` – Red Color Masking in Hexagon Image

- Detects red color in `hexagon2.jpg`.
- Calculates red pixel ratio to image size.
- Inverts the mask to highlight non-red (black) areas.

---

### `q5()` – Histogram Equalization & Similarity

- Performs manual histogram equalization on `road.jpg`.
- Compares histograms of identical images to check similarity.
- Contains (commented) logic for histogram matching between two images.

---

### `q6()` – Thresholding Techniques on Text Images

- Part A: Global thresholding on `text1.tif` and `text2.tif`.
- Part B: Manual thresholding using neighborhood average.
- Part C: Adaptive thresholding with OpenCV’s built-in method.

---

### `q7()` – Fundus Image Processing

- Part A: Thresholds `fundus.jpg` to separate background and object.
- Part B: Detects largest contour to approximate the eyeball's boundary.
- (Optional) Calculates and displays diameter using enclosing circle.

---

## 🧠 Notable Utilities

- `findLines()`: Applies a directional kernel to find edges in 0°, 45°, 90°, 135° or central patterns.
- `equilization()`: Manually implements histogram equalization using pixel frequency and cumulative distribution.
- `similarity()`: Compares two equalized histograms to check image similarity.

---

## 📌 Notes

- Make sure the `data/` folder contains all required images.
- OpenCV GUI (`cv2.imshow`) is used for visual output and requires a local environment.
- Use `cv2.waitKey(0)` and close image windows to proceed to the next.
