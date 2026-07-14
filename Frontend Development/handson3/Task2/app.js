import { courses } from "./data.js";

// Select Grid

const courseGrid = document.querySelector(".course-grid");

// Render Courses

courses.forEach(course => {

    const article = document.createElement("article");

    article.className = "course-card";

    article.innerHTML = `

        <h3>${course.name}</h3>

        <p>Course Code : ${course.code}</p>

        <p>Grade : ${course.grade}</p>

        <span>Credits : ${course.credits}</span>

    `;

    courseGrid.appendChild(article);

});

// Calculate Total Credits

const totalCredits = courses.reduce(

    (sum, course) => sum + course.credits,

    0

);

// Display Total Credits

document.getElementById("total-credits").textContent =
`Total Credits Enrolled : ${totalCredits}`;