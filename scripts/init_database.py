from sqlalchemy import create_engine, text

def init_database():
    """Initialize the database schema"""
    try:
        engine = create_engine('postgresql://airflow:airflow@localhost:5432/airflow')
        
        with engine.connect() as conn:
            # Create schemas
            schemas = ['analytics_staging', 'intermediate', 'mart']
            for schema in schemas:
                conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
                print(f"✅ Created schema: {schema}")
                
        print("Database schema initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return False

if __name__ == "__main__":
    init_database()
