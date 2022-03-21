from fastapi import FastAPI
from mangum import Mangum
from routes.person_route import person_api_router
from routes.students_route import students_api_router
from routes.todos_route import todo_api_router

app = FastAPI()
app.include_router(person_api_router)
app.include_router(students_api_router)
app.include_router(todo_api_router)

handler = Mangum(app)