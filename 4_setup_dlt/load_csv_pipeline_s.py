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
    # Go up one level
    project_root = working_directory.parent
    csv_path = project_root / "3_analyze_csv_duckdb" / "INGEST_DATA" / "data" / "social media influencers - youtube.csv"
    
    data = load_csv_resource(csv_path, encoding = "latin1")
    
    pipeline = dlt.pipeline(pipeline_name="social_media", 
                            destination=dlt.destinations.duckdb(str(working_directory / "data" / "social_media.duckdb")))
    
    load_info = pipeline.run(data, table_name="social_media")
    print(load_info)
    