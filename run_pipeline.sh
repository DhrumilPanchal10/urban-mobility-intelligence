#!/bin/bash

echo "🚀 Urban Mobility Intelligence Platform"
echo "========================================"
echo "Started at: $(date)"
echo ""

# Check if required directories exist
if [ ! -d "dbt" ]; then
    echo "❌ Error: dbt directory missing! Recreating..."
    mkdir -p dbt/models/{staging,intermediate,mart}
    mkdir -p dbt/tests
fi

# Step 1: Initialize database
echo "🗄️  Step 1: Initializing database schemas..."
python scripts/init_database.py

# Step 2: Data Ingestion
echo "📥 Step 2: Downloading NYC Subway Data..."
python airflow/dags/data_ingestion.py

# Step 3: Database Transformations
echo "🔄 Step 3: Running Data Transformations..."
cd dbt
dbt run --models staging

# Step 4: Data Quality Check
echo "✅ Step 4: Running Data Quality Tests..."
dbt test
cd ..

echo ""
echo "🎉 Pipeline completed at: $(date)"
echo "📊 Your data is ready for analysis!"
echo ""
echo "💡 Access your data:"
echo "   - PostgreSQL: localhost:5432 (airflow/airflow)"
echo "   - Analytics schema: analytics_staging"
