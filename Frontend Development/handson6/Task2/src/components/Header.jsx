import { Link } from "react-router-dom";
import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function Header() {

  const { enrolledCourses } = useContext(EnrollmentContext);

  return (

    <nav>

      <Link to="/">Courses</Link> |{" "}

      <Link to="/profile">Profile</Link>

      <h3>Enrolled : {enrolledCourses.length}</h3>

    </nav>

  );

}

export default Header;