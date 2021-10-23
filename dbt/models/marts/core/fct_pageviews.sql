{{
    config(
        materialized='incremental',
        incremental_strategy='delete+insert'
    )
}}

select * from {{ ref('stg_pageviews') }}

{% if is_incremental() %}

  where pageview_time > (select max(pageview_time) from {{ this }})

{% endif %}
