# database operations

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('MYSQL_ROOT_PASSWORD', ''),
    'database': 'MovieDatabase'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def execute_query(query, params=None):
    with get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query, params or ())
            if query.strip().upper().startswith('SELECT'):
                return cursor.fetchall()
            conn.commit()
            return True

def get_table_data(table_name):
    """get all data from a table"""
    query = f"SELECT * FROM {table_name}"
    return execute_query(query)


def search_movies_by_title_filtered(title, min_rating=0, genre_filter=None, year_filter=None):
    """search movies by title with optional filters"""
    query = """
    SELECT DISTINCT m.Movie_id, m.Title, m.Release_year FROM Movie m
    WHERE m.Title LIKE %s
    """
    params = [f"%{title}%"]

    if min_rating > 0:
        query += """
        AND m.Movie_id IN (
            SELECT r.Movie_Movie_id
            FROM Review r
            WHERE r.Rating >= %s
        )
        """
        params.append(min_rating)

    if genre_filter:
        query += """
        AND m.Movie_id IN (
            SELECT bt.Movie_Movie_id
            FROM Belongs_to bt
            JOIN Genre g ON bt.Genre_Genre_id = g.Genre_id
            WHERE g.Category LIKE %s
        )
        """
        params.append(f"%{genre_filter}%")

    if year_filter:
        query += " AND m.Release_year = %s"
        params.append(year_filter)

    return execute_query(query, params)

def search_movies_by_actor_filtered(actor_name, min_rating=0, genre_filter=None, year_filter=None):
    """search movies by actor name with optional filters"""
    query = """
    SELECT DISTINCT m.Movie_id, m.Title, m.Release_year FROM Movie m
    JOIN Acts_in ai ON m.Movie_id = ai.Movie_Movie_id
    JOIN Actor a ON ai.Actor_Actor_id = a.Actor_id
    WHERE CONCAT(a.First_name, ' ', a.Last_name) LIKE %s
    """
    params = [f"%{actor_name}%"]

    if min_rating > 0:
        query += """
        AND m.Movie_id IN (
            SELECT r.Movie_Movie_id
            FROM Review r
            WHERE r.Rating >= %s
        )
        """
        params.append(min_rating)

    if genre_filter:
        query += """
        AND m.Movie_id IN (
            SELECT bt.Movie_Movie_id
            FROM Belongs_to bt
            JOIN Genre g ON bt.Genre_Genre_id = g.Genre_id
            WHERE g.Category LIKE %s
        )
        """
        params.append(f"%{genre_filter}%")

    if year_filter:
        query += " AND m.Release_year = %s"
        params.append(year_filter)

    return execute_query(query, params)

def search_movies_by_director_filtered(director_name, min_rating=0, genre_filter=None, year_filter=None):
    """search movies by director name with optional filters"""
    query = """
    SELECT DISTINCT m.Movie_id, m.Title, m.Release_year FROM Movie m
    JOIN Directed_by db ON m.Movie_id = db.Movie_Movie_id
    JOIN Director d ON db.Director_Director_id = d.Director_id
    WHERE CONCAT(d.First_name, ' ', d.Last_name) LIKE %s
    """
    params = [f"%{director_name}%"]

    if min_rating > 0:
        query += """
        AND m.Movie_id IN (
            SELECT r.Movie_Movie_id
            FROM Review r
            WHERE r.Rating >= %s
        )
        """
        params.append(min_rating)

    if genre_filter:
        query += """
        AND m.Movie_id IN (
            SELECT bt.Movie_Movie_id
            FROM Belongs_to bt
            JOIN Genre g ON bt.Genre_Genre_id = g.Genre_id
            WHERE g.Category LIKE %s
        )
        """
        params.append(f"%{genre_filter}%")

    if year_filter:
        query += " AND m.Release_year = %s"
        params.append(year_filter)

    return execute_query(query, params)

def search_movies_by_genre_filtered(genre, min_rating=0, year_filter=None):
    """search movies by genre with optional filters"""
    query = """
    SELECT DISTINCT m.Movie_id, m.Title, m.Release_year FROM Movie m
    JOIN Belongs_to bt ON m.Movie_id = bt.Movie_Movie_id
    JOIN Genre g ON bt.Genre_Genre_id = g.Genre_id
    WHERE g.Category LIKE %s
    """
    params = [f"%{genre}%"]

    if min_rating > 0:
        query += """
        AND m.Movie_id IN (
            SELECT r.Movie_Movie_id
            FROM Review r
            WHERE r.Rating >= %s
        )
        """
        params.append(min_rating)

    if year_filter:
        query += " AND m.Release_year = %s"
        params.append(year_filter)

    return execute_query(query, params)

def search_movies_by_year_filtered(year, min_rating=0, genre_filter=None):
    """search movies by year with optional filters"""
    query = "SELECT Movie_id, Title, Release_year FROM Movie WHERE Release_year = %s"
    params = [year]

    if min_rating > 0:
        query += """
        AND Movie_id IN (
            SELECT r.Movie_Movie_id
            FROM Review r
            WHERE r.Rating >= %s
        )
        """
        params.append(min_rating)

    if genre_filter:
        query += """
        AND Movie_id IN (
            SELECT bt.Movie_Movie_id
            FROM Belongs_to bt
            JOIN Genre g ON bt.Genre_Genre_id = g.Genre_id
            WHERE g.Category LIKE %s
        )
        """
        params.append(f"%{genre_filter}%")

    return execute_query(query, params)
