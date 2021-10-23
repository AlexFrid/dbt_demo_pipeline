{% snapshot users_historic_snapshot %}

{{
    config(
      target_schema='snapshots',
      strategy='check',
      unique_key='user_id',
      check_cols=['postcode'],
    )
}}

select
id as user_id,
postcode

from {{ source('operational_databases', 'users_extract') }}

{% endsnapshot %}