#!/usr/bin/env python3
"""
Simple Movie Database Creation Script

Creates the MovieDatabase with all tables and sample data.
"""

import mysql.connector
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def create_database():
    """create the movie database"""

    # simple connection config
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': os.getenv('MYSQL_ROOT_PASSWORD', ''),
        'database': 'MovieDatabase'
    }

    try:
        # connect and create database
        print("Connecting to MySQL...")
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        print("Creating tables...")

        # drop all tables if they exist (to handle re-runs)
        drop_tables = [
            "DROP TABLE IF EXISTS Acts_in",
            "DROP TABLE IF EXISTS Belongs_to",
            "DROP TABLE IF EXISTS Directed_by",
            "DROP TABLE IF EXISTS User",
            "DROP TABLE IF EXISTS Review",
            "DROP TABLE IF EXISTS Movie",
            "DROP TABLE IF EXISTS Genre",
            "DROP TABLE IF EXISTS Director",
            "DROP TABLE IF EXISTS Actor"
        ]

        for drop_sql in drop_tables:
            cursor.execute(drop_sql)

        # create all tables with their constraints
        tables_sql = [
            """CREATE TABLE Actor (
                Actor_id INT NOT NULL, First_name VARCHAR(45), Last_name VARCHAR(45),
                PRIMARY KEY (Actor_id)
            )""",
            """CREATE TABLE Director (
                Director_id INT NOT NULL, First_name VARCHAR(45), Last_name VARCHAR(45),
                PRIMARY KEY (Director_id)
            )""",
            """CREATE TABLE Genre (
                Genre_id INT NOT NULL, Category VARCHAR(45),
                PRIMARY KEY (Genre_id)
            )""",
            """CREATE TABLE Movie (
                Movie_id INT NOT NULL, Title VARCHAR(45), Release_year INT,
                PRIMARY KEY (Movie_id)
            )""",
            """CREATE TABLE Review (
                Review_id INT NOT NULL, Rating INT, Movie_Movie_id INT,
                PRIMARY KEY (Review_id),
                FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id)
            )""",
            """CREATE TABLE User (
                User_id VARCHAR(25) NOT NULL, email VARCHAR(45), Review_Review_id INT NOT NULL,
                PRIMARY KEY (User_id),
                FOREIGN KEY (Review_Review_id) REFERENCES Review (Review_id)
            )""",
            """CREATE TABLE Acts_in (
                Actor_Actor_id INT NOT NULL, Movie_Movie_id INT NOT NULL,
                PRIMARY KEY (Actor_Actor_id, Movie_Movie_id),
                FOREIGN KEY (Actor_Actor_id) REFERENCES Actor (Actor_id),
                FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id)
            )""",
            """CREATE TABLE Belongs_to (
                Genre_Genre_id INT NOT NULL, Movie_Movie_id INT NOT NULL,
                PRIMARY KEY (Genre_Genre_id, Movie_Movie_id),
                FOREIGN KEY (Genre_Genre_id) REFERENCES Genre (Genre_id),
                FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id)
            )""",
            """CREATE TABLE Directed_by (
                Movie_Movie_id INT NOT NULL, Director_Director_id INT NOT NULL,
                PRIMARY KEY (Movie_Movie_id, Director_Director_id),
                FOREIGN KEY (Director_Director_id) REFERENCES Director (Director_id),
                FOREIGN KEY (Movie_Movie_id) REFERENCES Movie (Movie_id)
            )"""
        ]

        for sql in tables_sql:
            cursor.execute(sql)

        # insert sample data
        cursor.executemany("INSERT INTO Actor VALUES (%s, %s, %s)", [
            (122856, 'Jack', 'Black'), (135795, 'Johnny', 'Depp'), (175966, 'Chris', 'Hemsworth'),
            (246802, 'Natalie', 'Portman'), (446902, 'Scarlett', 'Johansson'), (629578, 'Jennifer', 'Lawrence'),
            (754201, 'Marilyn', 'Monroe'), (853301, 'Morgan', 'Freeman'), (918273, 'Harrison', 'Ford'),
            (987654, 'Emma', 'Stone')
        ])

        cursor.executemany("INSERT INTO Director VALUES (%s, %s, %s)", [
            (113579, 'Alfred', 'Hitchcock'), (146802, 'Emilio', 'Fernandez'), (234680, 'Nora', 'Ephron'),
            (366802, 'Spike', 'Lee'), (586802, 'John', 'Huston'), (597913, 'Agnes', 'Varda'),
            (630246, 'Sidney', 'Lumet'), (723456, 'Chantal', 'Akerman'), (801234, 'Stanley', 'Kubrick'),
            (990123, 'Hayao', 'Miyazaki')
        ])

        cursor.executemany("INSERT INTO Genre VALUES (%s, %s)", [
            (334497, 'Science Fiction'), (456789, 'Action'), (542261, 'Western'), (670518, 'Comedy'),
            (732871, 'Fantasy'), (765903, 'Thriller'), (845309, 'Romance'), (846342, 'Adventure'),
            (956721, 'Horror'), (968025, 'Musical')
        ])

        cursor.executemany("INSERT INTO Movie VALUES (%s, %s, %s)", [
            (121798, 'Coraline', 2009), (121978, 'The Iron Giant', 1999), (294658, 'Toy Story', 1995),
            (305542, 'The Lion King', 1994), (478548, 'Coco', 2017), (585388, 'The Godfather', 1972),
            (614005, 'Spirited Away', 2001), (751896, 'Moana', 2016), (831719, 'Jaws', 1975),
            (896786, 'Up', 2009)
        ])

        cursor.executemany("INSERT INTO Review VALUES (%s, %s, %s)", [
            (123456, 78, 585388), (248420, 81, 831719), (270372, 89, 614005), (324700, 50, 121978),
            (398999, 80, 121978), (521197, 96, 478548), (649391, 43, 305542), (930639, 75, 294658),
            (969856, 67, 751896), (975311, 91, 896786)
        ])

        cursor.executemany("INSERT INTO User VALUES (%s, %s, %s)", [
            ('alice', 'alice@email.com', 969856), ('angrybirds', 'angrybirds@email.com', 270372),
            ('beefeater', 'beefeater@emai.com', 521197), ('bigbadhat', 'bigbadhat@email.com', 398999),
            ('blueberyy', 'blueberry@email.com', 649391), ('chicken', 'chicken@email.com', 324700),
            ('froggy', 'froggy@email.com', 123456), ('scarypear', 'scarypear@email.com', 930639),
            ('tennisfan', 'tennisfan@email.com', 975311), ('yellowbear', 'yellowbear@email.com', 248420)
        ])

        cursor.executemany("INSERT INTO Acts_in VALUES (%s, %s)", [
            (122856, 121798), (135795, 121798), (987654, 121798), (246802, 121978), (446902, 121978),
            (918273, 121978), (122856, 294658), (135795, 294658), (987654, 294658), (135795, 305542),
            (853301, 305542), (987654, 305542), (122856, 478548), (135795, 478548), (853301, 585388),
            (918273, 585388), (246802, 614005), (446902, 614005), (629578, 614005), (122856, 751896),
            (175966, 751896), (629578, 751896), (122856, 831719), (175966, 831719), (122856, 896786),
            (754201, 896786), (853301, 896786)
        ])

        cursor.executemany("INSERT INTO Belongs_to VALUES (%s, %s)", [
            (956721, 121798), (846342, 121978), (670518, 294658), (846342, 294658), (846342, 305542),
            (968025, 305542), (846342, 478548), (968025, 478548), (456789, 585388), (732871, 614005),
            (846342, 614005), (846342, 751896), (765903, 831719), (732871, 896786)
        ])

        cursor.executemany("INSERT INTO Directed_by VALUES (%s, %s)", [
            (585388, 113579), (121798, 146802), (478548, 146802), (751896, 146802), (831719, 234680),
            (585388, 366802), (896786, 586802), (121798, 597913), (121978, 597913), (121978, 630246),
            (614005, 723456), (305542, 801234), (305542, 990123)
        ])

        conn.commit()
        cursor.close()
        conn.close()

        print("Database setup complete!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Check your MySQL password in .env file")
        sys.exit(1)

if __name__ == "__main__":
    create_database()