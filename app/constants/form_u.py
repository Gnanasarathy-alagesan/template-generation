from openpyxl.styles import Border, Side, Font
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.helper_util import date_format
ROW_HEIGHT = 30
BORDER = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )
START_ROW = 4
SERIAL_COLUMN = 'A'
FONT_STYLE = Font(name='Times New Roman', size=9)
MAPPING = {
    'B': "Full Name",
    'F': {"header":"DOJ", "function": date_format, "params": ('%Y-%m-%d',)}
}
