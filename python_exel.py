# Section 1
import pandas as pd
files = ['https://github.com/datagy/mediumdata/raw/master/january.xlsx', 'https://github.com/datagy/mediumdata/raw/master/february.xlsx', 'https://github.com/datagy/mediumdata/raw/master/march.xlsx']
combined = pd.DataFrame()

# Section 2
for file in files:
  df = pd.read_excel(file, skiprows = 3)
  combined = combined.append(df, ignore_index = True)

# Section 3
combined.to_excel('combined.xlsx')

# Section 1
import openpyxl

files = [] #include paths to your files here
values = []

# Section 2
for file in files:
    wb = openpyxl.load_workbook(file)
    sheet = wb['Sheet1']
    value = sheet['F5'].value
    values.append(value)

# Section 1
import openpyxl

files = [] # Insert paths to files here

for file in files:
    wb = openpyxl.load_workbook(file)
    sheet = wb['Sheet1']
    sheet['F9'] = '=SUM(F5:F8)'
    sheet['F9'].style = 'Currency'
    wb.save(file)
