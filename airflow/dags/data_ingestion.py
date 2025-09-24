import requests
import pandas as pd
import zipfile
import io
import os
from datetime import datetime
from sqlalchemy import create_engine
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataIngestor:
    def __init__(self):
        self.data_dir = "/opt/airflow/data"
        self.db_engine = create_engine('postgresql://airflow:airflow@postgres:5432/airflow')
        
    def download_nyc_static_gtfs(self):
        """Download NYC MTA static GTFS data"""
        try:
            logger.info("Downloading NYC GTFS data...")
            url = "http://web.mta.info/developers/data/nyct/subway/google_transit.zip"
            response = requests.get(url)
            response.raise_for_status()
            
            # Create directory if it doesn't exist
            os.makedirs(f"{self.data_dir}/raw/nyc_gtfs", exist_ok=True)
            
            # Extract ZIP file
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
                zip_file.extractall(f"{self.data_dir}/raw/nyc_gtfs")
                
            logger.info("Successfully downloaded NYC GTFS data")
            return True
            
        except Exception as e:
            logger.error(f"Failed to download NYC GTFS data: {e}")
            return False
            
    def load_to_staging(self):
        """Load raw data to PostgreSQL staging tables"""
        try:
            logger.info("Loading data to staging tables...")
            
            # Load stops data
            stops_path = f"{self.data_dir}/raw/nyc_gtfs/stops.txt"
            if os.path.exists(stops_path):
                stops_df = pd.read_csv(stops_path)
                stops_df.to_sql('staging_stops', self.db_engine, if_exists='replace', index=False)
                logger.info(f"Loaded {len(stops_df)} stops to database")
            
            # Load routes data
            routes_path = f"{self.data_dir}/raw/nyc_gtfs/routes.txt"
            if os.path.exists(routes_path):
                routes_df = pd.read_csv(routes_path)
                routes_df.to_sql('staging_routes', self.db_engine, if_exists='replace', index=False)
                logger.info(f"Loaded {len(routes_df)} routes to database")
            
            logger.info("Successfully loaded data to staging tables")
            return True
            
        except Exception as e:
            logger.error(f"Failed to load data to staging: {e}")
            return False

def ingest_data():
    """Main data ingestion function"""
    logger.info("Starting data ingestion...")
    ingestor = DataIngestor()
    
    # Download static data
    if ingestor.download_nyc_static_gtfs():
        # Load to database
        ingestor.load_to_staging()
    
    logger.info("Data ingestion completed")

# Test function
def test_ingestion():
    """Test the ingestion locally"""
    ingestor = DataIngestor()
    ingestor.download_nyc_static_gtfs()
    ingestor.load_to_staging()

if __name__ == "__main__":
    test_ingestion()
