from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api import login_router
import uvicorn
app=FastAPI()
@app.get("/")
def default_route():
    return JSONResponse(
        content={
            "message":"Server is running"
        }
    )
app.include_router(router=login_router,prefix="/login",tags=["Login"])
if __name__=="__main__":
    uvicorn.run(app="main:app",reload=True)