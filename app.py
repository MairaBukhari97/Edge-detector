import streamlit as st
import numpy as np
import cv2
from PIL import Image

# basic app setup
st.set_page_config(layout="wide", page_title="Edge Detection Visualizer")

st.title("Edge Detection Visualizer")
st.write("Upload an image, choose an algorithm, and tweak parameters to see results.")

# ---------------- sidebar ----------------
st.sidebar.header("Controls")

# upload image
uploaded = st.sidebar.file_uploader("Upload an image (JPG/PNG/BMP)", type=["jpg", "jpeg", "png", "bmp"])

# choose algorithm
algo = st.sidebar.radio("Algorithm", ["Canny", "Sobel", "Laplacian"])

# toggle for auto update
realtime = st.sidebar.checkbox("Real-time update (automatically reprocess on change)", value=True)
apply_button = None
if not realtime:
    apply_button = st.sidebar.button("Apply")

# algo-specific settings
if algo == "Canny":
    st.sidebar.subheader("Canny parameters")
    low_th = st.sidebar.slider("Lower threshold", 0, 500, 50)
    high_th = st.sidebar.slider("Upper threshold", 0, 500, 150)
    blur_kernel = st.sidebar.selectbox("Gaussian kernel size", [1, 3, 5, 7, 9], index=2)
    sigma = st.sidebar.slider("Gaussian sigma", 0.0, 5.0, 1.0, 0.1)

elif algo == "Sobel":
    st.sidebar.subheader("Sobel parameters")
    sobel_ksize = st.sidebar.selectbox("Kernel size", [1, 3, 5, 7], index=1)
    direction = st.sidebar.radio("Gradient direction", ["X", "Y", "Both"])

elif algo == "Laplacian":
    st.sidebar.subheader("Laplacian parameters")
    lap_ksize = st.sidebar.selectbox("Kernel size (odd)", [1, 3, 5, 7], index=1)

# ---------------- helper functions ----------------

def load_image_to_cv2(uploaded_file):
    # convert uploaded image to cv2 format (BGR)
    img = Image.open(uploaded_file).convert("RGB")
    arr = np.array(img)
    cv_img = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    return cv_img

def preprocess_gray(cv_img, kernel=1, sigma=1.0):
    # convert to grayscale + optional blur
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    if kernel > 1:
        k = kernel if kernel % 2 == 1 else kernel + 1
        gray = cv2.GaussianBlur(gray, (k, k), sigmaX=sigma)
    return gray

def apply_canny(cv_img, low, high, blur_k, sigma):
    # main canny function
    gray = preprocess_gray(cv_img, kernel=blur_k, sigma=sigma)
    edges = cv2.Canny(gray, low, high)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

def apply_sobel(cv_img, ksize, direction):
    # main sobel function (handles X, Y or both)
    gray = preprocess_gray(cv_img)
    k = ksize if ksize % 2 == 1 else ksize + 1
    dx = dy = None

    if direction in ("X", "Both"):
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=k)
        dx = cv2.convertScaleAbs(sobelx)
    if direction in ("Y", "Both"):
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=k)
        dy = cv2.convertScaleAbs(sobely)

    # combine gradients if both used
    if dx is not None and dy is not None:
        mag = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)
        out = cv2.cvtColor(mag, cv2.COLOR_GRAY2RGB)
    else:
        single = dx if dx is not None else dy
        out = cv2.cvtColor(single, cv2.COLOR_GRAY2RGB)
    return out

def apply_laplacian(cv_img, ksize):
    # laplacian edge detection
    gray = preprocess_gray(cv_img)
    k = ksize if ksize % 2 == 1 else ksize + 1
    lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=k)
    lap_abs = cv2.convertScaleAbs(lap)
    return cv2.cvtColor(lap_abs, cv2.COLOR_GRAY2RGB)

# ---------------- main layout ----------------
col1, col2 = st.columns(2)

# left: original image
with col1:
    st.subheader("Input - Original Image")
    if uploaded:
        cv_img = load_image_to_cv2(uploaded)
        rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        st.image(rgb, use_container_width=True)
    else:
        st.info("Upload an image from the sidebar to start.")

# right: processed output
with col2:
    st.subheader("Output - Edge Detection Result")
    if uploaded:
        process_now = realtime or (apply_button is True)
        if process_now:
            # run selected algo
            if algo == "Canny":
                result = apply_canny(cv_img, low_th, high_th, blur_kernel, sigma)
                params = f"Lower threshold = {low_th}, Upper threshold = {high_th}, Gaussian kernel = {blur_kernel}, Sigma = {sigma}"
            elif algo == "Sobel":
                result = apply_sobel(cv_img, sobel_ksize, direction)
                params = f"Kernel size = {sobel_ksize}, Direction = {direction}"
            else:
                result = apply_laplacian(cv_img, lap_ksize)
                params = f"Kernel size = {lap_ksize}"
            
            # show result
            st.image(result, use_container_width=True)

            # show algo + params below
            st.markdown(f"✅ *Algorithm:* {algo}")
            st.markdown(f"*Parameters:* {params}")

        else:
            st.info("Adjust parameters and click Apply.")
    else:
        st.info("Output will appear here after uploading and applying.")

# ---------------- sidebar summary ----------------
st.sidebar.markdown("---")
st.sidebar.markdown(f"*Selected:* {algo}")
if uploaded:
    st.sidebar.markdown("Image uploaded ✓")
else:
    st.sidebar.markdown("No image uploaded")