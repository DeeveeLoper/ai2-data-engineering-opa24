import pandas as pd
from pathlib import Path

def read_data():
    # Navigate up two directories from current file and then to the data folder
    data_path = Path(__file__).parents[2] / "data"
    
    # Read Excel file, skipping the first 5 rows. And selecting the "Tabell 3" sheet
    df = pd.read_excel(data_path / "resultat-ansokningsomgang-2024.xlsx", skiprows=5, sheet_name="Tabell 3")
    
    return df

# This block only executes when running this file directly
if __name__ == "__main__":
    # Test the function and print column names for inspection
    df = read_data()
    print(df.columns)