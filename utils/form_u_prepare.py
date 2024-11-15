import os
import sys

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from constants.generic import *
from constants.master import *
from constants.form_u import *
from utils.helper_util import get_columns, copy_file
from openpyxl import load_workbook
from openpyxl.styles import Side

# Load the existing workbook


class FormU:

    def __init__(self, base_location, template_file, master_df, office_location):
        self.base_location = base_location
        self.office_location = office_location
        self.file_name = template_file
        os.makedirs(f"{self.base_location}/{STAGE}", exist_ok=True)
        os.makedirs(f"{self.base_location}/{OUTPUT}", exist_ok=True)
        self.template_file = f"{self.base_location}/{TEMPLATE}/{template_file}"
        self.stage_file = f"{self.base_location}/{STAGE}/{template_file}"
        self.output_file = f"{self.base_location}/{OUTPUT}/{office.get(office_location.upper())}-{template_file}"
        copy_file(self.template_file, self.stage_file)
        self.master_df = master_df
        self.thin_border = BORDER
        self.row_height = 30
        self.font_style = FONT_STYLE

    def populate(self):
        self.wb = load_workbook(self.stage_file)
        self.ws = self.wb.active
        columns = get_columns(MAPPING)
        columns.append(LOCATION)
        filtered_df = self.master_df[columns]
        filtered_df = filtered_df[
            filtered_df[LOCATION].str.upper() == self.office_location
        ]
        row_value = -1
        for _, row in filtered_df.iterrows():
            row_value = row_value + 1
            row_number = START_ROW + row_value
            cell_coordinate = f"{SERIAL_COLUMN}{row_number}"
            self.ws[cell_coordinate] = row_value + 1
            self.ws[cell_coordinate].font = self.font_style

            for key, value in MAPPING.items():
                column = key
                cell_coordinate = f"{column}{row_number}"
                if type(value) == dict:
                    header = value.get("header")
                    function = value.get("function")
                    params = value.get("params")
                    self.ws[cell_coordinate] = function(row[header], *params)
                else:
                    header = value
                    self.ws[cell_coordinate] = row[header]
            self.ws[cell_coordinate].font = self.font_style
            self.ws.row_dimensions[row_number].height = self.row_height
            for col in range(1, self.ws.max_column + 1):
                self.ws.cell(row=row_number, column=col).border = self.thin_border

    def save_file(self):
        self.wb.save(self.output_file)
