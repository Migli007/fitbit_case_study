import pandas as pd
from sqlalchemy import create_engine

excel_file = r"C:\Users\migli\OneDrive\Desktop\fitbit data\weight_log.xlsx"


# Load the Excel file
df = pd.read_excel(excel_file, sheet_name='weightLogInfo_merged')  # Change sheet_name if needed

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:%40Supermanredson1@localhost:5432/fitbit_data')

df = df.drop_duplicates()

# Upload data to PostgreSQL
df.to_sql('weight_log', engine, if_exists='replace', index=False)

print("Upload successful!")
