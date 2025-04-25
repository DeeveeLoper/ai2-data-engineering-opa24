/*
with job_ads as (select * from {{ source('job_ads', 'stg_ads') }})

select
    {{ dbt_utils.generate_surrogate_key(['occupation__label']) }} as occupation_id, -- surrogate key for occupation
    {{ dbt_utils.generate_surrogate_key(['id']) }} as job_details_id,
    {{dbt_utils.generate_surrogate_key(['employer__workplace', 'workplace_address__municipality'])}} as employer_id,
    vacancies,
    relevance,
    application_deadline
from job_ads
*/


with stg_job_ads as (select * from {{ source('job_ads', 'stg_ads') }})

select
    occupation__label,
    id,
    employer__workplace,
    workplace_address__municipality,
    number_of_vacancies as vacancies,
    relevance,
    application_deadline
from stg_job_ads
