# TextToSpeechFromImage

# ImageToSpeech

## Overview

**ImageToSpeech** is a Python-based project that allows users to extract text from images using Tesseract OCR (Optical Character Recognition) and convert the extracted text to speech using a Text-to-Speech (TTS) engine. This project can be particularly useful for accessibility applications, automated reading systems, and converting printed text into an audible format.

## Features

- **Text Extraction from Images**: Utilizes Tesseract OCR to recognize and extract text from images.
- **Text-to-Speech Conversion**: Converts the extracted text to audible speech using the `pyttsx3` TTS engine.
- **Interactive Control**: Allows users to stop the speech mid-way through a simple keyboard input.

## Requirements

- **Python 3.x**
- **Libraries**:
  - `pillow` (for image processing)
  - `pytesseract` (for OCR)
  - `pyttsx3` (for TTS)
- **Tesseract OCR**: Must be installed and properly configured.

## Installation

### Prerequisites

1. **Install Python 3.x**: Make sure Python is installed on your system.
2. **Install Tesseract OCR**:
   - Download and install Tesseract from: [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).
   - Note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`).

### Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/ImageToSpeech.git
    cd ImageToSpeech
    ```

2. **Install Python Libraries**:
    ```bash
    pip install pillow pytesseract pyttsx3
    ```

3. **Configure Tesseract Path**:
   - Update the path to the Tesseract executable in the script:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```
