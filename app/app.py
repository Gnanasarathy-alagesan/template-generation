from flask import Flask, render_template, request
import os, sys
from werkzeug.utils import secure_filename
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.main import intial_prep, prepare_form_u

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

base_location = os.getcwd()
SRC_FOLDER = f'{base_location}/app/source'
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

@app.route('/generate', methods=['GET'])
def generate_file():
    try:
        master_df = intial_prep()
        prepare_form_u(master_df)
        return 'File Uploaded successfully', 200
    
    except Exception as e:
        print(e)
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
