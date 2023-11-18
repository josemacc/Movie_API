from fastapi import  FastAPI
from fastapi.responses import HTMLResponse
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.users import login_router
app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(login_router)




@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


