<h1 align="center">🖼️ Edge Detection Visualizer</h1> <p align="center"> <b>An interactive web app built with Streamlit, OpenCV, and Python</b><br> Upload an image, choose an algorithm, and visualize edge detection in real-time. </p>
📖 Overview

The Edge Detection Visualizer is an educational and experimental web application designed to help users explore classical computer vision edge detection techniques — Canny, Sobel, and Laplacian.

With intuitive sliders and real-time updates, you can see how parameters like thresholds, blur, and kernel sizes affect detected edges.

✨ Features

✅ Upload Images — Supports .jpg, .jpeg, .png, and .bmp

✅ Choose Algorithms — Canny, Sobel, or Laplacian

✅ Real-Time Visualization — Automatically updates as you tweak parameters

✅ Manual Apply Mode — Optional "Apply" button for batch adjustments

✅ Side-by-Side Display — Compare original and processed images instantly

✅ Dynamic Parameter Summary — Displays current algorithm and settings

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/edge-detector.git
cd edge-detector

2️⃣ (Optional) Create a Virtual Environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3️⃣ Install Dependencies

Make sure Python 3.8+ is installed, then run:

pip install -r requirements.txt

▶️ Running the Application
streamlit run src/app.py


Then open the link shown in the terminal (usually http://localhost:8501
) in your web browser.

🧠 Algorithms Explained
🔹 Canny Edge Detection

A multi-stage algorithm that detects a wide range of edges using gradient intensity and direction, followed by thresholding and non-maximum suppression.

Adjustable parameters:

Lower / Upper Threshold

Gaussian Blur Kernel Size

Sigma (Standard Deviation)

🔹 Sobel Operator

Calculates gradients along the X and Y axes to highlight horizontal and vertical edges.

Adjustable parameters:

Kernel Size

Gradient Direction (X, Y, or Both)

🔹 Laplacian Operator

Detects edges by calculating the second derivative of the image — sensitive to noise but captures fine details.

Adjustable parameters:

Kernel Size

💡 Additional Highlights

Clean, responsive layout using Streamlit’s column system

Parameter validation (ensures valid odd kernel sizes)

Real-time mode toggle for performance control

Lightweight and fast — built entirely in Python

🧰 Tech Stack
Technology	Purpose
Python 3.8+	Core programming language
Streamlit	Web UI framework
OpenCV	Image processing backend
NumPy	Array and matrix operations
Pillow (PIL)	Image handling
📷 Example Output
<p align="center"> <img src="screenshots/Canny.JPG" alt="Canny Edge Detection Result" width="90%"><br> <b>Figure 1:</b> Canny Edge Detection </p> <p align="center"> <img src="screenshots/Sobel.JPG" alt="Sobel Edge Detection Result" width="90%"><br> <b>Figure 2:</b> Sobel Edge Detection </p> <p align="center"> <img src="screenshots/Laplacian.JPG" alt="Laplacian Edge Detection Result" width="90%"><br> <b>Figure 3:</b> Laplacian Edge Detection </p> <p align="center">✅ <b>Enjoy exploring edge detection interactively!</b> 🎨</p>

This will render beautifully on GitHub with:

Proper headings

Emojis

Code blocks for commands

Images displayed correctly

Clean lists and tables

If you want, I can also add a small “Parameters Guide” table for each algorithm to make it even more readable. Do you want me to do that?

You said:
It should bold all the headings. Okay? And it should not bold on Windows or on Linux. Please do it rightly.
ChatGPT said:

Got it! You want all headings bold, but leave platform instructions (Windows/macOS/Linux) unbolded. Here’s a fully corrected version following that rule:

🖼️ Edge Detection Visualizer
<p align="center"> <b>An interactive web app built with Streamlit, OpenCV, and Python</b><br> Upload an image, choose an algorithm, and visualize edge detection in real-time. </p>
📖 Overview

The Edge Detection Visualizer is an educational and experimental web application designed to help users explore classical computer vision edge detection techniques — Canny, Sobel, and Laplacian.

With intuitive sliders and real-time updates, you can see how parameters like thresholds, blur, and kernel sizes affect detected edges.

✨ Features

✅ Upload Images — Supports .jpg, .jpeg, .png, and .bmp

✅ Choose Algorithms — Canny, Sobel, or Laplacian

✅ Real-Time Visualization — Automatically updates as you tweak parameters

✅ Manual Apply Mode — Optional "Apply" button for batch adjustments

✅ Side-by-Side Display — Compare original and processed images instantly

✅ Dynamic Parameter Summary — Displays current algorithm and settings

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/edge-detector.git
cd edge-detector

2️⃣ (Optional) Create a Virtual Environment
python -m venv venv


On Windows: venv\Scripts\activate

On macOS/Linux: source venv/bin/activate

3️⃣ Install Dependencies

Make sure Python 3.8+ is installed, then run:

pip install -r requirements.txt

▶️ Running the Application
streamlit run src/app.py


Then open the link shown in the terminal (usually http://localhost:8501
) in your web browser.

🧠 Algorithms Explained
🔹 Canny Edge Detection

A multi-stage algorithm that detects a wide range of edges using gradient intensity and direction, followed by thresholding and non-maximum suppression.

Adjustable parameters:

Lower / Upper Threshold

Gaussian Blur Kernel Size

Sigma (Standard Deviation)

🔹 Sobel Operator

Calculates gradients along the X and Y axes to highlight horizontal and vertical edges.

Adjustable parameters:

Kernel Size

Gradient Direction (X, Y, or Both)

🔹 Laplacian Operator

Detects edges by calculating the second derivative of the image — sensitive to noise but captures fine details.

Adjustable parameters:

Kernel Size

💡 Additional Highlights

Clean, responsive layout using Streamlit’s column system

Parameter validation (ensures valid odd kernel sizes)

Real-time mode toggle for performance control

Lightweight and fast — built entirely in Python

🧰 Tech Stack
Technology	Purpose
Python 3.8+	Core programming language
Streamlit	Web UI framework
OpenCV	Image processing backend
NumPy	Array and matrix operations
Pillow (PIL)	Image handling
📷 Example Output
<p align="center"> <img src="screenshots/Canny.JPG" alt="Canny Edge Detection Result" width="90%"><br> <b>Figure 1:</b> Canny Edge Detection </p> <p align="center"> <img src="screenshots/Sobel.JPG" alt="Sobel Edge Detection Result" width="90%"><br> <b>Figure 2:</b> Sobel Edge Detection </p> <p align="center"> <img src="screenshots/Laplacian.JPG" alt="Laplacian Edge Detection Result" width="90%"><br> <b>Figure 3:</b> Laplacian Edge Detection </p> <p align="center">✅ <b>Enjoy exploring edge detection interactively!</b> 🎨</p>