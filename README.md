# Color Conversion Project

This project focuses on converting images from the RGB color space to other popular color spaces, including HSV, HSI, CMYK, and LAB. The implemented conversions are detailed in the color_conversion.py script.

## Usage

1. Ensure you have the required dependencies installed:

    ```bash
    pip install opencv-python numpy
    ```

2. Run the color conversion script:

    ```bash
    python color_conversion.py
    ```

3. Check the output images in the repository:

    - `cmyk_image.png`
    - `hsv_image 1.png`
    - `hsv_image 2.png`
    - `lab_image.png`

## Color Spaces Implemented

### 1. HSV (Hue, Saturation, Value)

The HSV color space represents colors using three components: Hue, Saturation, and Value. The conversion is detailed in the `hsv_image 1.png` output.

### 2. HSI (Hue, Saturation, Intensity)

HSI is another representation of color with components: Hue, Saturation, and Intensity. The conversion is detailed in the `hsv_image 2.png` output.

### 3. CMYK (Cyan, Magenta, Yellow, Key/Black)

CMYK is a color space used in color printing. The conversion is detailed in the `cmyk_image.png` output.

### 4. LAB (CIELAB)

LAB is a color space designed to be perceptually uniform. The conversion is detailed in the `lab_image.png` output.

## Image Samples

- Original Image: `Lenna.png`
- Output Images: `cmyk_image.png`, `hsv_image 1.png`, `hsv_image 2.png`, `lab_image.png`

## Note

- All output images are saved in the PNG format.

