import dlt
import requests
from pathlib import Path
import os

# --- create dlt.resource object ---

def get_resource(url, endpoint):
    yield requests.get(url + "/" + endpoint).json()
    
@dlt.source
def jobad_links_source():
    
    url = 'https://links.api.jobtechdev.se'
    endpoints = ["joblinks"]
    
    for endpoint in endpoints:
        yield dlt.resource(get_resource(url, endpoint), 
                           name=endpoint, 
                           write_disposition="replace")

    
# --- create a pipeline object ---

def run_pipeline_source():
    
    pipeline_source = dlt.pipeline(pipeline_name="jobad_links_pipeline",
                                   destination=dlt.destinations.duckdb(f"{working_directory}/jobad_links.duckdb"),
                                   dataset_name="staging")
    source = jobad_links_source()
        
    load_info_source = pipeline_source.run(source.with_resources("joblinks"))
    print(load_info_source)
    
if __name__ == "__main__":
    
    working_directory = Path(__file__).parent
    os.chdir(working_directory)
    
    run_pipeline_source()
    
    # Run: duckdb -ui jobad_links.duckdb
    

