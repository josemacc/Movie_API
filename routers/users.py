from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from fastapi.routing import APIRouter
from schemas.user import User

login_router = APIRouter()

@login_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user)
        return JSONResponse(status_code=200, content=token)

