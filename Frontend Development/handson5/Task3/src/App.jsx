import { useEffect, useState } from "react";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";
import "./App.css";

function App() {

  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Runs once when the component mounts
  useEffect(() => {

    async function fetchCourses() {

      try {

        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts?_limit=5"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch courses");
        }

        const data = await response.json();

        setCourses(data);

      } catch (err) {

        setError(err.message);

      } finally {

        setLoading(false);

      }
    }

    fetchCourses();

  }, []);

  // Runs whenever the courses state changes
  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  return (
    <div>

      <h1>Student Portal</h1>

      {loading && <h2>Loading...</h2>}

      {error && <h2>{error}</h2>}

      {!loading &&
        !error &&
        courses.map((course) => (
          <CourseCard
            key={course.id}
            id={course.id}
            title={course.title}
          />
        ))}

      <StudentProfile />

    </div>
  );
}

export default App;