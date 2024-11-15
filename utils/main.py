# importing packages
import os
import sys

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from constants.generic import *
from constants.master import COLUMNS, LOCATION
from utils.helper_util import *
from utils.form_u_prepare import FormU

# getting base path
base_location = os.getcwd()

# assigning actual path to variables


def intial_prep():
    # copy paste from template folder to stage
    os.makedirs(f"{base_location}/{SOURCE}", exist_ok=True)
    source = base_location + f"/{SOURCE}/master.xlsx"
    master_df = pd.read_excel(source)
    master_df.columns = COLUMNS
    master_df["Full Name"] = master_df["First Name"] + " " + master_df["Last Name"]
    master_df = master_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return master_df


def prepare_form_u(master_df):
    # Form U
    for location in master_df[LOCATION].unique():
        location = location.upper()
        form_u = FormU(
            base_location=base_location,
            template_file=f"Form_U.xlsx",
            master_df=master_df,
            office_location=location,
        )
        form_u.populate()
        form_u.save_file()
