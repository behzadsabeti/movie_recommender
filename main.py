import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
from dotenv import load_dotenv

from views import home

app = fastapi.FastAPI()

def configure():
    configure_routing()
    configure_env_var()


def configure_routing():
    # api.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)

def configure_env_var():
    load_dotenv()
    


if __name__ == '__main__':
    configure()
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configure()