from fastapi import FastAPI, HTTPException, Response, status
from schemas import CourseCreate, CourseUpdate, CourseResponse
app = FastAPI(
    title="REST API Best Practices",
    version="1.0"
)

courses = []


@app.get("/api/v1/courses/")
async def get_courses():
    return courses


@app.post(
    "/api/v1/courses/",
    status_code=status.HTTP_201_CREATED,
    response_model=CourseResponse
)
async def create_course(course: CourseCreate, response: Response):

    new_course = {
        "id": len(courses) + 1,
        **course.model_dump()
    }

    courses.append(new_course)

    response.headers["Location"] = (
        f"/api/v1/courses/{new_course['id']}"
    )

    return new_course


@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
async def update_course(
    course_id: int,
    course: CourseCreate
):

    for c in courses:
        if c["id"] == course_id:

            c.update(course.model_dump())

            return c

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
async def patch_course(
    course_id: int,
    course: CourseUpdate
):

    for c in courses:
        if c["id"] == course_id:

            updates = course.model_dump(
                exclude_unset=True
            )

            c.update(updates)

            return c

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(course_id: int):

    for c in courses:
        if c["id"] == course_id:

            courses.remove(c)

            return

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )