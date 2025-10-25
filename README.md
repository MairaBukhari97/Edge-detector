<h1 style="text-align:center; color:#1a73e8; font-size:2.5em;">🖼️ Edge Detection Visualizer</h1>

<p style="text-align:center; font-weight:bold; font-size:1.1em;">
  An interactive web app built with Streamlit, OpenCV, and Python<br>
  Upload an image, choose an algorithm, and visualize edge detection in real-time.
</p>

<hr>

<h2 style="color:#1a73e8;">📖 Overview</h2>

<p>
The <strong>Edge Detection Visualizer</strong> is an educational and experimental web application designed to help users explore classical computer vision edge detection techniques — <strong>Canny</strong>, <strong>Sobel</strong>, and <strong>Laplacian</strong>.  
</p>

<p>
With intuitive sliders and real-time updates, you can see how parameters like thresholds, blur, and kernel sizes affect detected edges.
</p>

<hr>

<h2 style="color:#1a73e8;">✨ Features</h2>

<ul>
<li>✅ <strong>Upload Images</strong> — Supports <code>.jpg</code>, <code>.jpeg</code>, <code>.png</code>, and <code>.bmp</li>
<li>✅ <strong>Choose Algorithms</strong> — Canny, Sobel, or Laplacian</li>
<li>✅ <strong>Real-Time Visualization</strong> — Automatically update as you tweak parameters</li>
<li>✅ <strong>Manual Apply Mode</strong> — Optional "Apply" button for batch adjustments</li>
<li>✅ <strong>Side-by-Side Display</strong> — Compare the original and processed images instantly</li>
<li>✅ <strong>Dynamic Parameter Summary</strong> — Displays current algorithm and settings</li>
</ul>

<hr>

<h2 style="color:#1a73e8;">⚙️ Installation & Setup</h2>

<h3 style="color:#1a73e8;">1️⃣ Clone the Repository</h3>
<pre style="background-color:#eee; padding:10px; border-radius:6px;"><code>git clone https://github.com/yourusername/edge-detector.git
cd edge-detector</code></pre>

<h3 style="color:#1a73e8;">2️⃣ (Optional) Create a Virtual Environment</h3>
<pre style="background-color:#eee; padding:10px; border-radius:6px;"><code>python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate</code></pre>

<h3 style="color:#1a73e8;">3️⃣ Install Dependencies</h3>
<p>Make sure Python 3.8+ is installed, then run:</p>
<pre style="background-color:#eee; padding:10px; border-radius:6px;"><code>pip install -r requirements.txt</code></pre>

<h3 style="color:#1a73e8;">▶️ Running the Application</h3>
<pre style="background-color:#eee; padding:10px; border-radius:6px;"><code>streamlit run src/app.py</code></pre>
<p>Then open the link shown in the terminal (usually <code>http://localhost:8501</code>) in your web browser.</p>

<hr>

<h2 style="color:#1a73e8;">🧠 Algorithms Explained</h2>

<h3 style="color:#1a73e8;">🔹 Canny Edge Detection</h3>
<p>A multi-stage algorithm that detects a wide range of edges using gradient intensity and direction, followed by thresholding and non-maximum suppression.</p>
<p><strong>Adjustable parameters:</strong></p>
<ul>
<li>Lower / Upper Threshold</li>
<li>Gaussian Blur Kernel Size</li>
<li>Sigma (Standard Deviation)</li>
</ul>

<h3 style="color:#1a73e8;">🔹 Sobel Operator</h3>
<p>Calculates gradients along the X and Y axes to highlight horizontal and vertical edges.</p>
<p><strong>Adjustable parameters:</strong></p>
<ul>
<li>Kernel Size</li>
<li>Gradient Direction (X, Y, or Both)</li>
</ul>

<h3 style="color:#1a73e8;">🔹 Laplacian Operator</h3>
<p>Detects edges by calculating the second derivative of the image — sensitive to noise but captures fine details.</p>
<p><strong>Adjustable parameters:</strong></p>
<ul>
<li>Kernel Size</li>
</ul>

<hr>

<h2 style="color:#1a73e8;">💡 Additional Highlights</h2>
<ul>
<li>Clean, responsive layout using Streamlit’s column system</li>
<li>Parameter validation (ensures valid odd kernel sizes)</li>
<li>Real-time mode toggle for performance control</li>
<li>Lightweight and fast — built entirely in Python</li>
</ul>

<hr>

<h2 style="color:#1a73e8;">🧰 Tech Stack</h2>
<table style="width:80%; margin:auto; border-collapse:collapse;">
<tr><th style="border:1px solid #ddd; padding:8px;">Technology</th><th style="border:1px solid #ddd; padding:8px;">Purpose</th></tr>
<tr><td style="border:1px solid #ddd; padding:8px;">Python 3.8+</td><td style="border:1px solid #ddd; padding:8px;">Core programming language</td></tr>
<tr><td style="border:1px solid #ddd; padding:8px;">Streamlit</td><td style="border:1px solid #ddd; padding:8px;">Web UI framework</td></tr>
<tr><td style="border:1px solid #ddd; padding:8px;">OpenCV</td><td style="border:1px solid #ddd; padding:8px;">Image processing backend</td></tr>
<tr><td style="border:1px solid #ddd; padding:8px;">NumPy</td><td style="border:1px solid #ddd; padding:8px;">Array and matrix operations</td></tr>
<tr><td style="border:1px solid #ddd; padding:8px;">Pillow (PIL)</td><td style="border:1px solid #ddd; padding:8px;">Image handling</td></tr>
</table>

<hr>

<h2 style="color:#1a73e8;">📷 Example Output</h2>

<p style="text-align:center;">
  <img src="screenshots/Canny.JPG" alt="Canny Edge Detection Result" style="width:90%;"><br>
  <strong>Figure 1:</strong> Canny Edge Detection
</p>

<p style="text-align:center;">
  <img src="screenshots/Sobel.JPG" alt="Sobel Edge Detection Result" style="width:90%;"><br>
  <strong>Figure 2:</strong> Sobel Edge Detection
</p>

<p style="text-align:center;">
  <img src="screenshots/Laplacian.JPG" alt="Laplacian Edge Detection Result" style="width:90%;"><br>
  <strong>Figure 3:</strong> Laplacian Edge Detection
</p>

<p style="text-align:center;">✅ <strong>Enjoy exploring edge detection interactively!</strong> 🎨</p>
