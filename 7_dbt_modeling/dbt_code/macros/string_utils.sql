-- macros/capitalize_first_letter.sql
{% macro capitalize_first_letter(column) %}
  case
    when {{ column }} is null then null
    else upper(substr({{ column }}, 1, 1)) || lower(substr({{ column }}, 2))
  end
{% endmacro %}

-- models/your_model.sql
with src_employer as (
  select * from {{ ref('src_employer') }}
)

select
  {{ capitalize_first_letter("coalesce(workplace_city, 'stad ej specificerat')") }} as workplace_city
from src_employer
