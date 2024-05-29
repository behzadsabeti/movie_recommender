import psycopg2
from psycopg2 import OperationalError
import os


def get_db_conn():
    try:
        print("Attempting to connect to the database...")

        conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            port=os.getenv('POSTGRES_PORT'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            database=os.getenv('POSTGRES_DATABASE'),
            sslmode='require',
        )

        print("Successfully connected to the database.")
        return conn

    except OperationalError as e:
        print(f"OperationalError: {e}")
        raise

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def get_top_n_movies(n):
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("select url_name, name, year, poster_url from pop_movies order by rating_count DESC;")
    movies = cursor.fetchall()
    conn.close()
    movies = movies[:n]
    return movies


def get_movie_info(movies: list):
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("select poster_url, name, url_name from pop_movies where url_name in {};".format(tuple(movies)))
    info = cursor.fetchall()
    conn.close()
    return info

