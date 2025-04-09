WITH staging_data AS (
    SELECT * FROM ads.staging.data_field_job_ads
)

SELECT headline, description__text FROM staging_data

