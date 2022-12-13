import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/photos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
IMG_SIZE = 300
CATEGORIES = ["cardboard","glass","metal","paper","plastic","trash"]
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/ping", methods=["GET"], strict_slashes=False)
def app_check():
    return app.response_class(
        status=200, response="App is still running.", content_type="application/json"
    )


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
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
            return redirect(url_for('process_file', name=filename))
    return render_template('index.html')


@app.route('/prediction/<name>', methods=['POST'])
def process_file(name):
    # return send_from_directory(app.config["UPLOAD_FOLDER"], name)
    if lr:
        try:
            json_ = request.json
    print(json_)
    query = pd.get_dummies(pd.DataFrame(json_))
    query = query.reindex(columns=rnd_columns, fill_value=0)
    predict = list(lr.predict(query))
    return jsonify({‘prediction’: str(predict)})except:return jsonify({‘trace’: traceback.format_exc()})
    else:
    print(‘Model
    not good’)
    return (‘Model is not good’)

@app.route("/badresult", methods=["POST"], strict_slashes=False)
def bad_result():
    try:
        bad_result_name = ""
        bad_result_photo = ""
    except KeyError:
        return app.response_class(status=400)

    if bad_result_name == "_" or bad_result_photo == "":
        return app.response_class(status=400)


if __name__ == '__main__':
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = ID_Model(num_classes=len(CATEGORIES))
    model.load_state_dict(torch.load('TrashRecog/model.pth', map_location=device))
    model = model.to(device)
    model.eval()
    print("Model Loading Completed")

    app.run(host="localhost", port=5000)
