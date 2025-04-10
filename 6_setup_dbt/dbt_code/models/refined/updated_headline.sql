WITH staging_data AS (
    -- SELECT * FROM ads.staging.original_headline
    SELECT * FROM {{ ref('original_headline') }} -- This is the ref function that references. Jinja template  
)

SELECT 
    CASE
        WHEN headline = 'Data Engineer' THEN 'Junior data engineer'
        ELSE headline
    END AS job_title
FROM staging_data
