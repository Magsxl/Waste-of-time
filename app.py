import base64
import io
import os
from base64 import encodebytes
import requests
import pandas as pd
import torch as torch
import PIL.Image
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory, jsonify, json
from werkzeug.utils import secure_filename

from model import ID_Model, CATEGORIES, predictions

UPLOAD_FOLDER = '/photos'
ALLOWED_EXTENSIONS = {'jpg', 'png'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_image(image_path):
    pil_img = PIL.Image.open(image_path, mode='r')  # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG')  # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')  # encode as base64
    return encoded_img


def decode_image(coded_image: str):
    decoded_image = PIL.Image.open(io.BytesIO(base64.b64decode(str(coded_image))))
    image_rgb = decoded_image.convert("RGB")
    return image_rgb


@app.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
    #     f = request.files['file']
    #     f.save(secure_filename(f.filename))
    #     return 'file uploaded successfully', app.response_class(status=200)
    # else:
    #     'file uploading error', app.response_class(status=400)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            res = requests.post(url_for('process_file', _external=True), json={"image": get_image(
                os.path.join(app.config['UPLOAD_FOLDER'], filename))})
            if res.ok:
                print(res.json())
            return redirect(url_for('home'))

    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def process_file():
    image = decode_image(request.json["image"])
    modelResult = model.predictions(image)

    return app.response_class(
        response=json.dumps(modelResult).encode("utf8"), content_type="application/json"
    )


if __name__ == '__main__':
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = ID_Model(num_classes=len(CATEGORIES))
    model.load_state_dict(torch.load('model.pth', map_location=device))
    model = model.to(device)
    model.eval()
    print("Model Loading Completed")

    app.run(host="localhost", port=5000)
