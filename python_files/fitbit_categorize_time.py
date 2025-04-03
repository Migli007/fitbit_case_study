import pandas as pd
from sqlalchemy import create_engine

# Create engine for PostgreSQL connection
engine = create_engine('postgresql://postgres:%40Supermanredson1@localhost:5432/fitbit_data')

table_name = "daily_activity"  # Actual table name

# Load the data from PostgreSQL
df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

def get_day_of_week(date):
    if pd.notnull(date):
        return date.strftime('%A')  # Extract the full day name (e.g., 'Monday')
    return None

if 'ActivityDate' in df.columns:
    # Ensure 'ActivityDate' is treated as a datetime object
    df['ActivityDate'] = pd.to_datetime(df['ActivityDate'], errors='coerce')  # Convert to datetime

    # Add 'Day of Week' column
    df['Day of Week'] = df['ActivityDate'].apply(get_day_of_week)

    print("'Day of Week' column added successfully.")
else:
    print("Column 'ActivityDate' not found. Skipping day of week categorization.")

# Re-upload the modified DataFrame to PostgreSQL (use 'replace' or 'append' depending on needs)
df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Updated table '{table_name}' with 'Day of Week' successfully.")
