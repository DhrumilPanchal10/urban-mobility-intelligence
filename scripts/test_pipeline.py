import sys
import os
import pandas as pd
from sqlalchemy import create_engine, text
import subprocess

def test_database():
    """Test database connection and data"""
    try:
        engine = create_engine('postgresql://airflow:airflow@localhost:5432/airflow')
        with engine.connect() as conn:
            # Check if our tables exist
            tables = conn.execute(text("""
                SELECT table_name, table_schema 
                FROM information_schema.tables 
                WHERE table_schema IN ('public', 'analytics_staging')
            """)).fetchall()
            
            print("📊 Database tables:")
            for table in tables:
                print(f"   - {table[1]}.{table[0]}")
            
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_dbt():
    """Test dbt models"""
    try:
        result = subprocess.run(['dbt', 'debug'], cwd='dbt', capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ dbt connection working")
            return True
        else:
            print(f"❌ dbt test failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ dbt test error: {e}")
        return False

def main():
    print("🚀 Testing Urban Mobility Pipeline")
    print("=" * 50)
    
    tests = [test_database, test_dbt]
    results = []
    
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test {test.__name__} failed: {e}")
            results.append(False)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("💫 Pipeline is ready!")
    else:
        print("❌ Some tests failed")

if __name__ == "__main__":
    main()
