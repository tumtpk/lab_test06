from fastapi import APIRouter
from datetime import date

person_api_router = APIRouter()

@person_api_router.get("/service/getage")
async def get_test(year:int = 0):
    # age = current_year - year_dob
    current_year = date.today().year + 543
    if year == 0 :
        return {"error": "input not equal zero"}
    elif year > current_year:
        return {"error": "input more than current year"}
    else:
        age = current_year - year
        return {"age": age}