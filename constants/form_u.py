# Standard library imports
import os
import sys

from openpyxl.styles import Border
from openpyxl.styles import Font
from openpyxl.styles import Side

# Third-party imports

# This allows importing modules located in the parent directory, even if they are outside the default module resolution paths.
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Local application imports
from utils.helper_util import date_format

# FORM_U Constants
ROW_HEIGHT = 30

# Borders style of the cell
BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)
# From where the records has to be populated
START_ROW = 4

# Serial number column in the Excel
SERIAL_COLUMN = "A"

# Font Style
FONT_STYLE = Font(name="Times New Roman", size=9)

# Mapping Form U columns with Master data columns
MAPPING = {
    "B": "Full Name",
    "F": {"header": "DOJ", "function": date_format, "params": ("%Y-%m-%d",)},
}
