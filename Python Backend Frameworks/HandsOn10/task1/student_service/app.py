from flask import Flask, jsonify
from models import db, Student

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if Student.query.count() == 0:
        db.session.add(Student(name="Afifa"))
        db.session.commit()


@app.route("/api/students")
def get_students():

    students = Student.query.all()

    return jsonify([
        {
            "id": s.id,
            "name": s.name
        }
        for s in students
    ])


if __name__ == "__main__":
    app.run(port=5002, debug=True)