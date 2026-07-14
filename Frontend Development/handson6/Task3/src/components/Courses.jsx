import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";

const courses = [
  { id: 1, name: "React" },
  { id: 2, name: "Java" },
  { id: 3, name: "Python" },
];

function Courses() {

  const dispatch = useDispatch();

  return (
    <div>

      <h2>Courses</h2>

      {courses.map((course) => (
        <div key={course.id}>

          <h3>{course.name}</h3>

          <button
            onClick={() => dispatch(enroll(course))}
          >
            Enroll
          </button>

        </div>
      ))}

    </div>
  );
}

export default Courses;