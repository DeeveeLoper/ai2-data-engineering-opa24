with job_ads as (select * from {{ ref('src_job_ads') }})

-- SELECT * FROM job_ads

select
    -- {{ dbt_utils.generate_surrogate_key(['occupation__label']) }}, -- hashing
    {{ dbt_utils.generate_surrogate_key(['occupation__label']) }} as occupation_id, -- occupation_id
    {{ dbt_utils.generate_surrogate_key(['id']) }} as job_details_id, -- job_details_is
    {{ dbt_utils.generate_surrogate_key(['employer__workplace', 'workplace_address__municipality']) }} -- workplace_id
    as employer_id,
    vacancies,
    relevance,
    application_deadline
from job_ads