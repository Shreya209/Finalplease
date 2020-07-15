import os
from flask import Flask, render_template, request
from PIL import Image
from pytesseract import image_to_string
# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'
# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# route and function to handle the home page
@app.route('/')
def home_page():
    return render_template('index.html')
# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
   
        file = request.form['img']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            image = Image.open(UPLOAD_FOLDER + file.filename, mode='r')
            Extracted = image_to_string(image)
   # extract the text and display it
            return render_template('upload.html',
                                   extracted_text=Extracted)

    elif request.method == 'GET':
        return render_template('upload.html')

if (__name__) == ('__main__') :
    app.run()
