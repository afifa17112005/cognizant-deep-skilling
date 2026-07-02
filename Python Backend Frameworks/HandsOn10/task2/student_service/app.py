from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Afifa"
    }
]

@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll_student(id):

    data = request.get_json()
    course_id = data.get("course_id")

    try:
        response = requests.get(
            f"http://127.0.0.1:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({
                "message": "Course not found"
            }), 404

        course = response.json()

        return jsonify({
            "message": "Enrollment Successful",
            "student_id": id,
            "course": course
        })

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service Unavailable"
        }), 503


if __name__ == "__main__":
    app.run(port=5002, debug=True)