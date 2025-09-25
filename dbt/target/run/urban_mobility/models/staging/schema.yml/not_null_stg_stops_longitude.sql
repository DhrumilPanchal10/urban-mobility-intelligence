
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select longitude
from "airflow"."analytics_analytics"."stg_stops"
where longitude is null



  
  
      
    ) dbt_internal_test