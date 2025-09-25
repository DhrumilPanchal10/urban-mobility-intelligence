
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select route_long_name
from "airflow"."analytics_analytics"."stg_routes"
where route_long_name is null



  
  
      
    ) dbt_internal_test