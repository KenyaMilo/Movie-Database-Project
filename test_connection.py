import os
import mysql.connector

# Load environment variables if you’re using a .env file locally
from dotenv import load_dotenv
load_dotenv()

# Database configuration using environment variables
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'movie-database-moviedatabaseproj.d.aivencloud.com'),
    'user': os.getenv('MYSQL_USER', 'avnadmin'),
    'password': os.getenv('MYSQL_PASSWORD'),  # removed hardcoded password
    'database': os.getenv('MYSQL_DATABASE', 'defaultdb'),
    'port': int(os.getenv('MYSQL_PORT', 25490)),
    'ssl_ca': 'ca-certificate.pem'
}

# Test connection
try:
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Error connecting to database: {e}")

