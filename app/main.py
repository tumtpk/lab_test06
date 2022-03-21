from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"This is our secret key value:" }

handler = Mangum(app)