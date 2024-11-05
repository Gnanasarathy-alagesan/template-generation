# importing packages
import pandas as pd
import os
from constants.generic import *
from utils.helper_util import *
from utils.form_u_prepare import FormU

# getting base path
base_location = os.getcwd()

#assigning actual path to variables
template = f"{base_location}/{TEMPLATE}/"
stage = f"{base_location}/{STAGE}/"
output = f"{base_location}/{OUTPUT}/"

# copy paste from template folder to stage
copy_all_files(template, stage)

source = base_location + f"/{SOURCE}/master.xlsx"

master_df = pd.read_excel(source)
master_df["Full Name"] = master_df["First Name"] + ' ' + master_df["Last Name"]



#Form U

chennai = FormU(file_location = f"{stage}/Form_U.xlsx", master_df = master_df, office_location = 'Chennai', output_path = output)
chennai.populate()
chennai.save_file()







