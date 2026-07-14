import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  function enroll(course) {

    if (!enrolledCourses.find(c => c.id === course.id)) {
      setEnrolledCourses([...enrolledCourses, course]);
    }

  }

  function remove(courseId) {

    setEnrolledCourses(
      enrolledCourses.filter(course => course.id !== courseId)
    );

  }

  return (

    <EnrollmentContext.Provider
      value={{
        enrolledCourses,
        enroll,
        remove
      }}
    >

      {children}

    </EnrollmentContext.Provider>

  );

}