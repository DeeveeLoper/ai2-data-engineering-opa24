import dlt
import pandas as pd
from pathlib import Path
import os

@dlt.resource(write_disposition="replace")
def load_csv_resource(file_path: str, **kwargs):
    df = pd.read_csv(file_path, **kwargs)
    yield df
    
if __name__ == "__main__":
    
    working_directory = Path(__file__).parent
    csv_path = working_directory / "data" / "NetflixOriginals.csv"
    
    data = load_csv_resource(csv_path, encoding = "latin1")
    
    pipeline = dlt.pipeline(pipeline_name="movies",
                           destination=dlt.destinations.duckdb(str(working_directory / "data" / "movies.duckdb")))
    
    load_info = pipeline.run(data, table_name="netflix")
    print(load_info)
    