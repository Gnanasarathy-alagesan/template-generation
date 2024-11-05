from openpyxl.styles import Border, Side, Font
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
    'B': "Full Name"
}