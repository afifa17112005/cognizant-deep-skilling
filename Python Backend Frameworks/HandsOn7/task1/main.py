from fastapi import FastAPI, HTTPException, status

from schemas import CourseCreate, CourseUpdate

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

courses = []


@app.get("/")
async def root():
    return {"message": "HandsOn 7 Task 1 Running"}


@app.post(
    "/api/courses/",
    status_code=status.HTTP_201_CREATED
)
async def create_course(course: CourseCreate):

    new_course = {
        "id": len(courses) + 1,
        **course.model_dump()
    }

    courses.append(new_course)

    return new_course


@app.put("/api/courses/{course_id}")
async def update_course(
    course_id: int,
    course: CourseUpdate
):

    for c in courses:

        if c["id"] == course_id:

            update_data = course.model_dump(
                exclude_unset=True
            )

            c.update(update_data)

            return c

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


@app.delete(
    "/api/courses/{course_id}",
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


@app.get("/api/courses/{course_id}/students")
async def get_students(course_id: int):

    for c in courses:

        if c["id"] == course_id:

            return {
                "course_id": course_id,
                "students": [
                    "Alice",
                    "Bob"
                ]
            }

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )