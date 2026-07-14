import { Routes, Route } from "react-router-dom";

import Header from "./components/Header";

import CoursesPage from "./pages/CoursesPage";

import ProfilePage from "./pages/ProfilePage";

function App() {

  return (

    <div>

      <Header />

      <Routes>

        <Route
          path="/"
          element={<CoursesPage />}
        />

        <Route
          path="/profile"
          element={<ProfilePage />}
        />

      </Routes>

    </div>

  );

}

export default App;