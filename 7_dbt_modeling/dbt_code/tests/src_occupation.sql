with stg_job_ads as (
    select * from {{ source('job_ads', 'stg_ads') }}
)

-- Return rows where critical fields are null or missing
select 
    id,
    headline
from stg_job_ads
where 
    occupation__concept_id is null
    or occupation_group__concept_id is null
    or occupation_field__concept_id is null
    or occupation__label is null
    or occupation_group__label is null
    or occupation_field__label is null