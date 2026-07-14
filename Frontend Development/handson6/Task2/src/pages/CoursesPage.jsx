import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

const courses = [

  { id: 1, name: "React" },

  { id: 2, name: "Java" },

  { id: 3, name: "Python" }

];

function CoursesPage() {

  const { enroll } = useContext(EnrollmentContext);

  return (

    <div>

      <h2>Courses</h2>

      {courses.map(course => (

        <div key={course.id}>

          <h3>{course.name}</h3>

          <button onClick={() => enroll(course)}>
            Enroll
          </button>

        </div>

      ))}

    </div>

  );

}

export default CoursesPage;