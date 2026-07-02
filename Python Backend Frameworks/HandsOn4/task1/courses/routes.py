from flask import Blueprint, jsonify, request

bp = Blueprint("courses", __name__)

courses = []


@bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses)


@bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()

    courses.append(data)

    return jsonify(data), 201