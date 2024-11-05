from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


SRC_FOLDER = '../source'
app.config['UPLOAD_FOLDER'] = SRC_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
    
        # Handle file upload
        if 'srcFile' not in request.files:
            print("No file part")
            return 'No file part', 400
        
        file = request.files['srcFile']
        if file.filename == '':
            print("No selected file")
            return 'No selected file', 400
        
        if file:
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return 'File Uploaded successfully', 200
    
    except Exception as e:
        print(e)
        return str(e), 500


if __name__ == '__main__':
    app.run(debug=True)
