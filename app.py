# Standard library imports
import os
import sys

from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

# Third-party imports

# This allows importing modules located in the parent directory, even if they are outside the default module resolution paths.
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Local application imports
from utils.main import prepare_master, prepare_form_u
from constants.generic import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


# Preparing source location
base_location = os.getcwd()
SRC_FOLDER = os.path.join(base_location, "source")
os.makedirs(SRC_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = SRC_FOLDER

# Global variable to store the DataFrame
master_df = None


@app.route("/upload", methods=["POST"])
def upload_file():
    """
    Uploadind the source files
    """
    try:
        # Handle file upload
        if "srcFiles" not in request.files:
            print("No file part")
            return "No file part", 400

        files = request.files.getlist("srcFiles")
        print(files)
        if len(files) == 0:
            print("No selected file")
            return "No selected file", 400

        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        return "File(s) Uploaded successfully", 200

    except Exception as e:
        print(e)
        return str(e), 500


@app.route("/generate", methods=["GET"])
def generate_file():
    """
    To prepare templates
    """
    try:
        global master_df
        prepare_form_u(master_df)
        return "File Uploaded successfully", 200

    except Exception as e:
        print(e)
        return str(e), 500


@app.route("/validate", methods=["GET"])
def validate_src():
    """
    Check all necessary sources are uploaded for preparing templates
    """
    try:
        directory = app.config["UPLOAD_FOLDER"]

        existing_files = os.listdir(directory)
        print("existing files:")
        print(existing_files)
        print("directory:")
        print(directory)

        # Check if each file in file_list exists in the directory
        file_status = {
            file_name: file_name in existing_files for file_name in SRC_FILE_LIST
        }

        print("file status:")
        print(file_status)

        if all(file_status.values()):
            return "Source file(s) present", 200
        else:
            return "Some files are missing.", 404
    except FileNotFoundError:
        print("Directory not found.")
        return str(e), 404
    except Exception as e:
        print(e)
        return str(e), 500


@app.route("/prepare", methods=["GET"])
def prepare_source():
    """
    Prepare master_df globally with transformation applied
    """
    try:
        global master_df
        master_df = prepare_master()
        return "Source prepared successfully", 200

    except Exception as e:
        print(e)
        return str(e), 500


if __name__ == "__main__":
    app.run(debug=False)
