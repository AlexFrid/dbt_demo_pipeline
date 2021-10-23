with 

users as (

    select * from {{ ref('dim_users') }}

),

pageviews as (

    select * from {{ ref('fct_pageviews') }}

),

pageviews_agg as (

    select 
        user_id,
        DATE_TRUNC('HOUR', pageview_time) as pageview_time,
        count(*) as number_of_pageviews 

    from pageviews
    group by 1,2

),

pageviews_users as (

    select 
        pageviews_agg.user_id,
        pageviews_agg.number_of_pageviews,
        users.postcode as postcode_current,
        pageviews_agg.pageview_time

    from pageviews_agg
    inner join users on pageviews_agg.user_id=users.user_id

),

final as (

    select * from pageviews_users

)

select * from final