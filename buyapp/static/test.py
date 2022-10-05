import  io as StringIO
from xlsxwriter.workbook import Workbook
output = StringIO.StringIO()
book = Workbook(output)
sheet = book.add_worksheet(unicode('シート名', 'utf_8'))
# A列は15、B〜E列は20で幅を設定しています。自由に設定してください。
sheet.set_column('A:A', 15)
sheet.set_column('B:E', 20)
# ヘッダー。第一引数が行、第二引数が列を表しています。
sheet.write(0, 0, uicode('A列のヘッダー', 'utf_8'))
sheet.write(0, 1, uicode('B列のヘッダー', 'utf_8'))
sheet.write(0, 2, uicode('C列のヘッダー', 'utf_8'))
sheet.write(0, 3, uicode('D列のヘッダー', 'utf_8'))
sheet.write(0, 4, uicode('E列のヘッダー', 'utf_8'))