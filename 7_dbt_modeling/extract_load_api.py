import dlt
import requests
import json
from pathlib import Path
import os


def _get_ads(url_for_search, params):
    headers = {"accept": "application/json"}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  # check for http errors
    return json.loads(response.content.decode("utf8"))


@dlt.resource(write_disposition="append")
def jobsearch_resource(params):
    """
    params should include at least:
      - "q": your query
      - "limit": page size (e.g. 100)
    """
    url = "https://jobsearch.api.jobtechdev.se"
    url_for_search = f"{url}/search"
    limit = params.get("limit", 100)
    offset = 0

    while True:
        # build this page's params
        page_params = dict(params, offset=offset)
        data = _get_ads(url_for_search, page_params)

        hits = data.get("hits", [])
        if not hits:
            # no more results
            break

        # yield each ad on this page
        for ad in hits:
            yield ad

        # if fewer than a full page was returned, we're done
        if len(hits) < limit or offset > 1900:
            break

        offset += limit


def run_pipeline(query, table_name, occupation_fields):
    # Create absolute path to the 7_dbt_modeling folder
    target_dir = Path(__file__).parent.resolve()
    db_path = target_dir / "ads_data_warehouse.duckdb"
    
    pipeline = dlt.pipeline(
        pipeline_name="jobads_demo",
        destination=dlt.destinations.duckdb(str(db_path)),  # Use absolute path
        dataset_name="staging",
    )

    for occupation_field in occupation_fields:
        params = {"q": query, "limit": 100, "occupation-field": occupation_field}
        load_info = pipeline.run(
            jobsearch_resource(params=params), table_name=table_name
        )
        print(f"Occupation field: {occupation_field}")
        print(load_info)
        print(f"Database path: {db_path}")  # Print the path to confirm


if __name__ == "__main__":
    # Ensure we're in the correct working directory
    script_dir = Path(__file__).parent.resolve()
    os.chdir(script_dir)
    print(f"Working directory set to: {script_dir}")

    query = ""
    table_name = "job_ads"

    # Technical focus, "Hälso sjukvård", "Pedagogik"
    occupation_fields = ("6Hq3_tKo_V57", "NYW6_mP6_vwf", "MVqp_eS8_kDZ")

    run_pipeline(query, table_name, occupation_fields)