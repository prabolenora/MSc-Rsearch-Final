import cv2
import pytesseract
import time
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\tesseract.exe'

def calculate_accuracy(recognized_text, ground_truth_text):
    recognized_text = recognized_text.lower()
    ground_truth_text = ground_truth_text.lower()

    total_characters = len(ground_truth_text)
    correct_characters = sum(r == g for r, g in zip(recognized_text, ground_truth_text))

    accuracy = (correct_characters / total_characters) * 100

    return accuracy


# Load the image
image = cv2.imread('cam 12.jpg')

# Preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform text extraction
start_time = time.time()

invert = 255 - thresh
recognized_text = pytesseract.image_to_string(Image.fromarray(invert), lang='eng', config='--psm 6')

processing_time = time.time() - start_time

# Calculate accuracy (assuming you have ground truth text)
ground_truth_text = "T35JM"
accuracy = calculate_accuracy(recognized_text, ground_truth_text)

# Print the results
print("Recognized Text:")
print(recognized_text)
print("Accuracy:", accuracy)
print("Processing Time:", processing_time)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
