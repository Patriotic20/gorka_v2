from fastapi import FastAPI
import uvicorn
from src.api import router as main_api

app = FastAPI()

app.include_router(main_api)

if __name__ == "__main__":
    uvicorn.run("main:app" , reload=True)