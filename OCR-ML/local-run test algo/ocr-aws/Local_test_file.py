import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd= r'C:\Users\User\AppData\Local\tesseract.exe'

# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('cam 12.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print('invert')
print(data)

data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
print('thresh')
print(data)

data = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')
print('gray')
print(data)
data = pytesseract.image_to_string(blur, lang='eng', config='--psm 6')
print('blur')
print(data)
data = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
print('image')
print(data)
data = pytesseract.image_to_string(opening, lang='eng', config='--psm 6')
print('opening')
print(data)

# cv2.imshow('thresh', thresh)
# cv2.imshow('opening', opening)
# cv2.imshow('invert', invert)
cv2.imshow('image', image)
cv2.waitKey()
text = pytesseract.image_to_string(Image.open('cam 12.jpg'))
print(text)