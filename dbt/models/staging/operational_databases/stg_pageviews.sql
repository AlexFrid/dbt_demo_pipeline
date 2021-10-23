select
    UUID_STRING() as pageview_id,
    user_id,
    timestamp as pageview_time,
    url

from {{ source('operational_databases', 'pageviews_extract') }}
