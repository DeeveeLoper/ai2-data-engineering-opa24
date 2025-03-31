import pandas as pd
import dlt
import os
import duckdb
from pathlib import Path

# Define a resource to be used in the pipeline
@dlt.resource(write_disposition="replace")
#@dlt.resource(write_disposition="append")

def load_csv_resource(file_path: str, **kwargs):
    # Read the CSV file with pandas
    df = pd.read_csv(file_path, **kwargs)
    yield df
    
if __name__ == '__main__':
    # Get the current directory where the script is running
    working_directory = Path(__file__).parent 
    
    os.chdir(working_directory)
    # Build the path to the CSV file
    csv_path = working_directory / "data" / "NetflixOriginals.csv"
    
    data = load_csv_resource(csv_path, encoding = "latin1")
    print(list(data))
    
    # Create a DLT pipeline
    pipeline = dlt.pipeline(
        pipeline_name="movies", # Name of the pipeline
        destination=dlt.destinations.duckdb(
            # DuckDB database path (must be converted to string)
            str(working_directory / "data" / "movies.duckdb")
        ),
        # Creates a schema named "staging" in the databas
        dataset_name="staging"
    )
    # Run the pipeline with CSV data and specify the table name
    load_info = pipeline.run(load_csv_resource(csv_path, encoding="latin1"), table_name="netflix")
    
    print(load_info)
