from pydantic import BaseModel


class EnrollmentCreate(BaseModel):
    student_email: str