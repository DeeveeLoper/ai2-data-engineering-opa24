import dlt
import requests
from pathlib import Path
import os

# --- create dlt.resource ---

def get_ads(url_for_search, params):
    response = requests.get(url_for_search, params=params)
    return response.json()

@dlt.resource(write_disposition="replace")
def jobsearch_resource(params):
    url = "https://jobsearch.api.jobtechdev.se"
    url_for_search = f"{url}/search"
    
    for ad in get_ads(url_for_search, params)["hits"]:
        yield ad

# --- create a pipeline object ---

def run_pipeline(query, table_name):
        
    pipeline = dlt.pipeline(pipeline_name="jobsearch",
                            destination=dlt.destinations.duckdb(f"{working_directory}/ads_resource.duckdb"),
                            dataset_name="staging",
    )
    
    params = {"q": query, "limit": 100}
    load_info = pipeline.run(jobsearch_resource(params=params), table_name=table_name)
    print(load_info)

if __name__ == "__main__":
     # Confirm the working directory is the one storing the .dlt folder, and storing the file
    working_directory = Path(__file__).parent
    os.chdir(working_directory)
    
    # Execute the pipeline for data loading
    query = "data engineer"
    table_name = "data_field_job_ads"
    run_pipeline(query, table_name)
    
    # Run: duckdb -ui ads_resource.duckdb