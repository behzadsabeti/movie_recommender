from psycopg2 import OperationalError
import fastapi
from fastapi import Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates
import psycopg2
from typing import List, Dict
from data import create_model
import os

templates = Jinja2Templates('templates')
router = fastapi.APIRouter()

user_ratings = {}

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


@router.get('/')
def index(request: Request):
    movies = get_top_n_movies(50)
    return templates.TemplateResponse('home/index.html', {'request': request, "movies": movies})


@router.post("/rate_movies")
async def rate_movies(request: Request, selected_movies: List[str] = Form([])):
    
    movies_info = get_movie_info(selected_movies)
    print(movies_info)
    return templates.TemplateResponse("home/rate_movies.html", {"request": request, "movies_info": movies_info})
    

@router.post("/show_recommendations")
async def recommend_movies(request: Request, ratings: Dict[str, int]):

    # calling the model and pass the ratings dict
    print(ratings)
    global user_ratings
    user_ratings = ratings

    return ratings
    
    

@router.get("/show_recommendations")
async def show_recommendations(request: Request):
    recommendations = create_model.get_recommendations(user_ratings)
    movie_ids = [x[0] for x in recommendations]
    movies_info = get_movie_info(movie_ids)
    print(recommendations)
    
    return templates.TemplateResponse("home/recommendations.html", {"request": request, "movies_info": movies_info, "ratings": recommendations})

# @router.get('/favicon.ico')
# def favicon():
#     return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')