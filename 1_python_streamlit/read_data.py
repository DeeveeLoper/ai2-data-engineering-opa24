import pandas as pd
from pathlib import Path

def read_data():
    
    # Use parent to go up one level (from read_data.py to file)
    data_path = Path(__file__).parents[1] / "data"
    
    # Read the excel file, skipping the first 5 rows and selecting the "Tabell 3" sheet 
    df = pd.read_excel(data_path / "resultat-ansokningsomgang-2024.xlsx", skiprows=5, sheet_name="Tabell 3")
    return df

# Runs only when the script is executed directly
if __name__ == "__main__":
    # Call read_data() function to test it
    df = read_data()
    # Print column names to verify data was loaded correctly
    print(df.columns)
    