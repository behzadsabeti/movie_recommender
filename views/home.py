import fastapi
from fastapi import Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from typing import List, Dict

from data import create_model
from services import database_service
templates = Jinja2Templates('templates')
router = fastapi.APIRouter()

user_ratings = {}


@router.get('/')
def index(request: Request):
    movies = database_service.get_top_n_movies(50)
    return templates.TemplateResponse('home/index.html', {'request': request, "movies": movies})


@router.post("/rate_movies")
async def rate_movies(request: Request, selected_movies: List[str] = Form([])):
    
    movies_info = database_service.get_movie_info(selected_movies)
    print(movies_info)
    return templates.TemplateResponse("home/rate_movies.html", {"request": request, "movies_info": movies_info})
    

@router.post("/show_recommendations")
async def recommend_movies(request: Request, ratings: Dict[str, int]):

    # calling the model and pass the ratings dict
    global user_ratings
    user_ratings = ratings

    return ratings
    
    

@router.get("/show_recommendations")
async def show_recommendations(request: Request):
    recommendations = create_model.get_recommendations(user_ratings)
    movie_ids = [x[0] for x in recommendations]
    movies_info = database_service.get_movie_info(movie_ids)
    print(recommendations)
    
    return templates.TemplateResponse("home/recommendations.html", {"request": request, "movies_info": movies_info, "ratings": recommendations})

# @router.get('/favicon.ico')
# def favicon():
#     return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')