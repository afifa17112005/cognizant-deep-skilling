from flask import Flask, jsonify
from models import db, Course

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if Course.query.count() == 0:
        db.session.add(Course(
            title="Python",
            description="Python Programming"
        ))
        db.session.commit()


@app.route("/api/courses/<int:id>")
def get_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    return jsonify({
        "id": course.id,
        "title": course.title,
        "description": course.description
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)