select
    id as user_id,
    postcode

from {{ source('operational_databases', 'users_extract') }}