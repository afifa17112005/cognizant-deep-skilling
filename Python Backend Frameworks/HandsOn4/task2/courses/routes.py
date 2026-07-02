from flask import Blueprint, jsonify, request

bp = Blueprint("courses", __name__)

courses = []
next_id = 1


# Helper function
def make_response_json(data, status_code):
    return jsonify(data), status_code


# GET all courses
@bp.route("/", methods=["GET"])
def get_courses():
    return make_response_json(courses, 200)


# GET course by ID
@bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return make_response_json(course, 200)

    return make_response_json(
        {"error": "Course not found"},
        404
    )


# POST new course
@bp.route("/", methods=["POST"])
def add_course():
    global next_id

    data = request.get_json()

    if not data:
        return make_response_json(
            {"error": "Request body must be JSON"},
            400
        )

    required_fields = ["name", "code", "credits"]

    for field in required_fields:
        if field not in data:
            return make_response_json(
                {"error": f"{field} is required"},
                400
            )

    course = {
        "id": next_id,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses.append(course)
    next_id += 1

    return make_response_json(course, 201)


# DELETE course
@bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    global courses

    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return make_response_json(
                {"message": "Course deleted successfully"},
                200
            )

    return make_response_json(
        {"error": "Course not found"},
        404
    )