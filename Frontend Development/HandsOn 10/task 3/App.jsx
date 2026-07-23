import CoursesPage from "./pages/CoursesPage";
import ErrorPage from "./pages/ErrorPage";

function App() {

  return (

    <div>

      <h1>Student Portal</h1>

      <CoursesPage />

      {/* Uncomment this line to test Error Boundary */}

      {/* <ErrorPage /> */}

    </div>

  );

}

export default App;