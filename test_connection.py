import os
import mysql.connector

# Aiven credentials (replace with your actual values or use environment variables)
DB_CONFIG = {
    'host': 'movie-database-moviedatabaseproj.d.aivencloud.com',
    'user': 'avnadmin',
    'password': 'AVNS_D_C7o7Frov9AvXtM10R',
    'database': 'defaultdb',
    'port': 25490,
    'ssl_ca': 'ca-certificate.pem'
}

try:
    connection = mysql.connector.connect(**DB_CONFIG)
    print("Connection successful!")
    connection.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")

