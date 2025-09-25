
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select stop_name
from "airflow"."analytics_analytics"."stg_stops"
where stop_name is null



  
  
      
    ) dbt_internal_test