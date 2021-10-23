with 

users as (

    select * from {{ ref('users_historic_snapshot') }}

)

select * from users