import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.model import predict_tumor

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Helper function to validate file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error="No file selected.")
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Predict tumor class
            predicted_class, confidence = predict_tumor(file_path)

            return render_template('result.html', 
                                   prediction=predicted_class, 
                                   confidence=round(confidence * 100, 2))

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
