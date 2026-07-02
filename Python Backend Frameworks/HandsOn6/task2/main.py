from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db

app = FastAPI(
    title="Course Management API",
    version="2.0"
)


@app.get("/")
async def root():
    return {
        "message": "Task 2 Running"
    }


@app.get("/api/courses/")
async def read_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None,
    db: AsyncSession = Depends(get_db)
):
    return {
        "skip": skip,
        "limit": limit,
        "department_id": department_id
    }


@app.get("/api/courses/{course_id}")
async def read_course(course_id: int):
    return {
        "course_id": course_id
    }