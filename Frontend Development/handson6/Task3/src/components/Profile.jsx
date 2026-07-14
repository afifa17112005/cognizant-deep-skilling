import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";

function Profile() {

  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <div>

      <h2>My Courses</h2>

      {enrolledCourses.length === 0 ? (
        <p>No Courses Enrolled</p>
      ) : (
        enrolledCourses.map((course) => (
          <div key={course.id}>

            <h3>{course.name}</h3>

            <button
              onClick={() =>
                dispatch(unenroll(course.id))
              }
            >
              Remove
            </button>

          </div>
        ))
      )}

    </div>
  );
}

export default Profile;