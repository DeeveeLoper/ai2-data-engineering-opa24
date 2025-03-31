import pandas as pd
from pathlib import Path

def read_data():
    # Get the directory where read_data.py is located
    project_root = Path(__file__).resolve().parent
    # Path to the data directory
    data_path = project_root / "data"
    # Read the excel file, skipping the first 5 rows and selecting the "Tabell 3" sheet 
    df = pd.read_excel(data_path / "resultat-ansokningsomgang-2024.xlsx", skiprows=5, sheet_name="Tabell 3")
    return df

# Runs only when the script is executed directly
if __name__ == "__main__":
    # Call read_data() function to test it
    df = read_data()
    # Print column names to verify data was loaded correctly
    print(df.columns)
    