from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware
from routers import videos
from db import create_all_tables


app = FastAPI(lifespan=create_all_tables) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(videos.router)

@app.get("/")
def root():
    return{"Hola": "Mundo"}
