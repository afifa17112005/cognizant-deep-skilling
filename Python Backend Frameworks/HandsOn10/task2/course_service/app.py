from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "title": "Python",
        "description": "Python Programming"
    },
    {
        "id": 2,
        "title": "Java",
        "description": "Java Programming"
    }
]


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):
    for course in courses:
        if course["id"] == id:
            return jsonify(course)

    return jsonify({"message": "Course not found"}), 404


if __name__ == "__main__":
    app.run(port=5001, debug=True)