from PIL import Image
import pytesseract
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
 
def extract_text_from_image(image_path):
    #OCR on the image
    extracted_text = pytesseract.image_to_string(Image.open(image_path))
    return extracted_text

def main():
    image_path = r"C:\JN\messi.jpg"  
    print(f"Processing image: {image_path}")
    text = extract_text_from_image(image_path)
    print("Extracted text:", text)
    speak(text)

if __name__ == "__main__":
    main()
