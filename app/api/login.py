from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.model import LoginModel
login_router=APIRouter()
@login_router.get("/")
def default():
    return JSONResponse(
        content={
            "message":"Default route for login ✅",
            "statusCode":200
        },
        status_code=200
    )
@login_router.post("/loginUser")
def login_user(user:LoginModel):
    userData=user.model_dump()
    print(f"User data is {userData}")
    return JSONResponse(
        content={
            "message":"Success",
            "email":user.email,
            "data":userData,
        }
    )




