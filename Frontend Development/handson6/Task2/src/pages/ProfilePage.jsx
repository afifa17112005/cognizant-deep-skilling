import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function ProfilePage() {

  const { enrolledCourses, remove } =
    useContext(EnrollmentContext);

  return (

    <div>

      <h2>My Courses</h2>

      {enrolledCourses.length === 0 ? (

        <p>No Courses Enrolled</p>

      ) : (

        enrolledCourses.map(course => (

          <div key={course.id}>

            <h3>{course.name}</h3>

            <button
              onClick={() => remove(course.id)}
            >
              Remove
            </button>

          </div>

        ))

      )}

    </div>

  );

}

export default ProfilePage;