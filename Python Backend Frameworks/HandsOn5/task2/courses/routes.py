from flask import Blueprint, jsonify, request
from models import db, Course, Student

bp = Blueprint("courses", __name__)


# GET all courses
@bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


# GET course by ID
@bp.route("/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())


# POST new course
@bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()

    required = ["name", "code", "credits", "department_id"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# PUT update course
@bp.route("/<int:id>", methods=["PUT"])
def update_course(id):
    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data.get("name", course.name)
    course.code = data.get("code", course.code)
    course.credits = data.get("credits", course.credits)
    course.department_id = data.get("department_id", course.department_id)

    db.session.commit()

    return jsonify(course.to_dict())


# DELETE course
@bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully"})


# GET students enrolled in a course
@bp.route("/<int:id>/students", methods=["GET"])
def get_students(id):
    course = Course.query.get_or_404(id)

    students = [
        enrollment.student.to_dict()
        for enrollment in course.enrollments
    ]

    return jsonify(students)