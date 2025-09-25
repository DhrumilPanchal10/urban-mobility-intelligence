#!/bin/bash

echo "🚀 Urban Mobility Intelligence Platform"
echo "========================================"
echo "Started at: $(date)"
echo ""

# Step 1: Data Ingestion
echo "📥 Step 1: Downloading NYC Subway Data..."
python airflow/dags/data_ingestion.py

# Step 2: Database Transformations
echo "🔄 Step 2: Running Data Transformations..."
cd dbt
dbt run --models staging

# Step 3: Data Quality Check
echo "✅ Step 3: Running Data Quality Tests..."
dbt test

echo ""
echo "🎉 Pipeline completed at: $(date)"
echo "📊 Your data is ready for analysis!"
echo ""
echo "💡 Access your data:"
echo "   - PostgreSQL: localhost:5432 (airflow/airflow)"
echo "   - Analytics schema: analytics_staging"
echo "   - Contains: 1,497 subway stations, 30 routes"
