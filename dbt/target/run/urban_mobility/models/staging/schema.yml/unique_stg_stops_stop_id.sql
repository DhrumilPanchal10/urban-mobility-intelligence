
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    stop_id as unique_field,
    count(*) as n_records

from "airflow"."analytics_analytics"."stg_stops"
where stop_id is not null
group by stop_id
having count(*) > 1



  
  
      
    ) dbt_internal_test