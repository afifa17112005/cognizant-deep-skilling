from fastapi import FastAPI, HTTPException
from schemas import Course

app = FastAPI(
    title="REST API Best Practices",
    version="2.0",
    description="API Versioning, Pagination and Standard Error Responses"
)

courses = [
    {"id": 1, "name": "Python", "code": "CS101", "credits": 4},
    {"id": 2, "name": "Database", "code": "CS102", "credits": 3},
    {"id": 3, "name": "Networking", "code": "CS103", "credits": 4},
    {"id": 4, "name": "AI", "code": "CS104", "credits": 5},
    {"id": 5, "name": "ML", "code": "CS105", "credits": 4},
]


# API Versioning + Pagination
@app.get("/api/v1/courses/")
async def get_courses(page: int = 1, page_size: int = 2):

    start = (page - 1) * page_size
    end = start + page_size

    results = courses[start:end]

    next_page = page + 1 if end < len(courses) else None
    previous_page = page - 1 if page > 1 else None

    return {
        "count": len(courses),
        "next": next_page,
        "previous": previous_page,
        "results": results
    }


# Search
@app.get("/api/v1/courses/search")
async def search_course(q: str):

    results = []

    for course in courses:
        if q.lower() in course["name"].lower() or q.lower() in course["code"].lower():
            results.append(course)

    return results


# Standard Error Response
@app.get("/api/v1/courses/{course_id}")
async def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail={
            "error": {
                "code": "NOT_FOUND",
                "message": f"Course with id {course_id} does not exist",
                "field": None
            }
        }
    )