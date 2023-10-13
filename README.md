# Canny, Sobel and Prewitt Edge Detection Techniques in Python

This Python code demonstrates different image edge detection techniques using the OpenCV library. It loads an image, applies various edge detection methods, and displays the results using Matplotlib.

## Getting Started

These instructions will help you understand the code and use it for your own image processing tasks.

### Prerequisites

- Python (3.x recommended)
- OpenCV (Open Source Computer Vision Library)
- NumPy
- Matplotlib

### Installation

To install the required libraries, you can use `pip`:

```bash
pip install opencv-python numpy matplotlib
```

## Code Description

The code performs edge detection using the following techniques:

1. **Canny Edge Detection**:
   - Canny edge detection is applied to the original image.
   - It identifies strong, weak, and non-edge pixels based on specified threshold values (100 and 200 in this case).

2. **Sobel Edge Detection**:
   - Sobel edge detection is applied to a Gaussian blurred version of the original image.
   - The Sobel function is used to calculate the gradient in both the x and y directions.
   - The results are combined to form the final Sobel edge image.

3. **Prewitt Edge Detection**:
   - Prewitt edge detection is applied using custom 3x3 kernels for x and y directions.
   - The filter2D function convolves the image with these kernels to compute the gradient in both directions.

## Usage

1. Clone this repository or download the code to your local machine.

2. Replace 'OIP.jpeg' with the path to your own image file that you want to apply edge detection to.

3. Run the code using your Python interpreter.

4. The script will display the original image and the results of Canny, Sobel, and Prewitt edge detection techniques using Matplotlib.

5. Close the Matplotlib window to exit the application.

## Example

Here's how you can run the code:

```python
python program.py
```

The output will be a Matplotlib window showing the original image and the results of the edge detection techniques.

## Acknowledgments

- [OpenCV](https://opencv.org/): Open Source Computer Vision Library
- [Matplotlib](https://matplotlib.org/): Plotting library for Python

## Authors

- [Hamza Iftikhar] - [Your GitHub Profile]([https://github.com/yourusername](https://github.com/hamzaiftkhar))

## Acknowledgments

- This code is for educational purposes and can be used as a reference for image processing tasks.
- Feel free to customize and extend this code according to your requirements.
