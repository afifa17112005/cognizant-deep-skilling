import { Link } from "react-router-dom";

const courses = [
  { id: 1, name: "React" },
  { id: 2, name: "Java" },
  { id: 3, name: "Python" }
];

function CoursesPage() {
  return (
    <div>
      <h2>Courses</h2>

      {courses.map((course) => (
        <div key={course.id}>
          <Link to={`/courses/${course.id}`}>
            {course.name}
          </Link>
        </div>
      ))}
    </div>
  );
}

export default CoursesPage;