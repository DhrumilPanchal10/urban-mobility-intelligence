

with source_data as (
    select
        stop_id,
        stop_name,
        stop_lat as latitude,
        stop_lon as longitude
    from "airflow"."public"."staging_stops"
)

select
    *,
    current_timestamp as loaded_at
from source_data