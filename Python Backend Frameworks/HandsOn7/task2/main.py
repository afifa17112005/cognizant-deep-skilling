from fastapi import FastAPI, BackgroundTasks, status

from schemas import EnrollmentCreate

app = FastAPI(
    title="Course Management API",
    version="1.0",
    description="HandsOn 7 Task 2",
    contact={
        "name": "Student",
        "email": "student@example.com"
    }
)


def send_confirmation_email(email: str):
    print(f"Sending confirmation to {email}")


@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    status_code=status.HTTP_201_CREATED,
    summary="Create Enrollment",
    description="Create a new enrollment and send a confirmation email."
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        send_confirmation_email,
        enrollment.student_email
    )

    return {
        "message": "Enrollment created",
        "student_email": enrollment.student_email
    }