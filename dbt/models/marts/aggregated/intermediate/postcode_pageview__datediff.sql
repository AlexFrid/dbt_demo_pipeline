{{
    config(
        materialized='incremental',
        incremental_strategy='delete+insert'
    )
}}

with

users_historic as (

    select * from {{ ref('dim_users_historic') }}

),

pageviews as (

    select * from {{ ref('fct_pageviews') }}

),

datediff as (

    select 
        pageview_id,
        pageviews.user_id,
        pageview_time,
        postcode,
        DATEDIFF(day, dbt_valid_from, pageview_time) as diff_days

    from pageviews
    inner join users_historic on pageviews.user_id=users_historic.user_id

),

min_difference as (

    select 
        pageview_id,
        min(diff_days) as min_difference_bewteen_pageview_and_postcode_time

    from datediff
    group by 1

),

final as (

    select
        min_difference.pageview_id,
        datediff.user_id,
        datediff.postcode as postcode_historic,
        datediff.pageview_time

    from min_difference
    join datediff on min_difference.pageview_id=datediff.pageview_id

)

select * from final

{% if is_incremental() %}

    where pageview_time > (select max(pageview_time) from {{ this }})

{% endif %}