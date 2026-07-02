from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/api/enroll/<int:student_id>", methods=["POST"])
def enroll(student_id):

    data = request.get_json()

    try:
        response = requests.post(
            f"http://127.0.0.1:5002/api/students/{student_id}/enroll",
            json=data
        )

        return jsonify(response.json()), response.status_code

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Student Service Unavailable"
        }), 503


if __name__ == "__main__":
    app.run(port=5000, debug=True)