import { useState } from "react";
import coursesData from "./data";
import CourseCard from "./components/CourseCard";
import "./App.css";

function App() {

  const [courses] = useState(coursesData);

  const [searchTerm, setSearchTerm] = useState("");

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  function handleEnroll(id) {

    if (!enrolledCourses.includes(id)) {
      setEnrolledCourses([...enrolledCourses, id]);
    }

  }

  const filteredCourses = courses.filter(course =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>

      <h1>Student Portal</h1>

      <h3>Enrolled Courses : {enrolledCourses.length}</h3>

      <input
        type="text"
        placeholder="Search Course"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      {filteredCourses.map(course => (
        <CourseCard
          key={course.id}
          {...course}
          onEnroll={handleEnroll}
        />
      ))}

    </div>
  );
}

export default App;