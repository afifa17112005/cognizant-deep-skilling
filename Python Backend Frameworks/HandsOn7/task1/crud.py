from sqlalchemy import select

from models import Course


courses = []


def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    return None