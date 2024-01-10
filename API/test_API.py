from flask import Flask, json, request, jsonify, send_from_directory
import os
import urllib.request
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
 
app.secret_key = "caircocoders-ednalan"
 
UPLOAD_FOLDER = 'images'

# Maximal zulässige Dateigröße
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
@app.route('/')
def main():
    return 'Hauptseite'
 
# files[] ist der Schlüssel 
@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
 
 # Das request-Objekt enthält Daten, die in einer HTTP-Anfrage gesendet werden
    files = request.files.getlist('files[]')
     
    errors = {}
    success = False
     
    for file in files:      
        if file: 
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'
 
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    
# Man kann sich das Bild aus dem Ordner selber aussuchen 
@app.route('/image/<filename>')
def display_image(filename):
    return send_from_directory('images', filename)

#Wann soll diese Methode durchlaufen werden ?
def image_rotate(filename): 
    bild = "hallo1"
    myImage = Image.open(f"images\input_Images\{bild}.png")
    rotated_image = myImage.rotate(90, expand=True)
    rotated_image.show()
    rotated_image.save(f"images\processed_Images\{bild}p1.png")

 
if __name__ == '__main__':
    app.run(debug=True)