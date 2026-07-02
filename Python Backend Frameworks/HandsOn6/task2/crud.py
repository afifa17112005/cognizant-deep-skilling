from sqlalchemy import select

from models import Course


async def get_courses(db):
    result = await db.execute(select(Course))
    return result.scalars().all()