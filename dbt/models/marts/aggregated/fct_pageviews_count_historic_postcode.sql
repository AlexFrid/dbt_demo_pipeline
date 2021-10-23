with 

historic_postcode as (

    select * from {{ ref('postcode_pageview__datediff') }}

),

pageview_count as (

    select * from {{ ref('fct_pageviews_count_current_postcode') }}

),

historic_postcode_agg as (

    select
        user_id,
        postcode_historic

    from postcode_pageview__datediff
    group by 1,2

),

final as (

    select
        pageview_count.user_id,
        number_of_pageviews,
        postcode_historic,
        pageview_count.pageview_time

    from pageview_count
    inner join historic_postcode_agg where pageview_count.user_id=historic_postcode_agg.user_id

)

select * from final