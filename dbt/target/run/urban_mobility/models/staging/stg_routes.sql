
  create view "airflow"."analytics_analytics"."stg_routes__dbt_tmp"
    
    
  as (
    

with source_data as (
    select
        route_id,
        route_short_name,
        route_long_name,
        route_type,
        route_color,
        route_text_color
    from "airflow"."public"."staging_routes"
)

select
    *,
    current_timestamp as loaded_at
from source_data
  );