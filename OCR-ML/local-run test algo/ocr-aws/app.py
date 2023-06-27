from flask import Flask, request
from PIL import Image
import pytesseract
import json
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/ocr', methods=["POST"])
def index():
 if request.files.get("image") is None:
    return {'error': 'Image is missing'}
 url='https://docs.unity3d.com/Packages/com.unity.textmeshpro@3.2/manual/images/TMP_RichTextLineIndent.png'
 image = Image.open(requests.get(url, stream=True).raw)
 #image = Image.open(request.files["image"])
 context = {'content' : pytesseract.image_to_string(image)}
 print(pytesseract.image_to_string(image))
 text = pytesseract.image_to_string(Image.open(image))
 print(text)
 return context
