from fastapi import FastAPI
from routes.person_route import person_api_router

app = FastAPI()
app.include_router(person_api_router)