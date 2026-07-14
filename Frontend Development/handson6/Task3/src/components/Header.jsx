import { useSelector } from "react-redux";

function Header() {

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <header>
      <h1>Student Portal</h1>

      <h3>Enrolled: {enrolledCourses.length}</h3>
    </header>
  );
}

export default Header;