import { useParams, useNavigate } from "react-router-dom";

const courses = [
  { id: 1, name: "React" },
  { id: 2, name: "Java" },
  { id: 3, name: "Python" }
];

function CourseDetailPage() {

  const { courseId } = useParams();

  const navigate = useNavigate();

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return <h2>Course Not Found</h2>;
  }

  function handleEnroll() {
    alert("Enrolled Successfully!");
    navigate("/profile");
  }

  return (
    <div>

      <h2>{course.name}</h2>

      <p>Course ID: {course.id}</p>

      <button onClick={handleEnroll}>
        Enroll
      </button>

    </div>
  );
}

export default CourseDetailPage;