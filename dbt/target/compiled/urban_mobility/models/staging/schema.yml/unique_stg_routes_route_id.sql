
    
    

select
    route_id as unique_field,
    count(*) as n_records

from "airflow"."analytics_analytics"."stg_routes"
where route_id is not null
group by route_id
having count(*) > 1


