// Import course array

import { courses } from "./data.js";

console.log("===== COURSE DETAILS =====");

// Destructuring inside a loop

courses.forEach(course => {

    const { name, credits } = course;

    console.log(`Course : ${name} | Credits : ${credits}`);

});

console.log("--------------------------------");

// map()

const formattedCourses = courses.map(course =>
    `${course.code} — ${course.name} (${course.credits} credits)`
);

console.log("Formatted Course List");

console.log(formattedCourses);

console.log("--------------------------------");

// filter()

const creditCourses = courses.filter(course => course.credits >= 4);

console.log("Courses with Credits >= 4");

console.log(creditCourses);

console.log("Count :", creditCourses.length);

console.log("--------------------------------");

// reduce()

const totalCredits = courses.reduce(
    (total, course) => total + course.credits,
    0
);

console.log(`Total Credits = ${totalCredits}`);

console.log("--------------------------------");

// Arrow Function

const displayCourse = course =>
    `${course.name} has Grade ${course.grade}`;

console.log("Course Grades");

courses.forEach(course => {

    console.log(displayCourse(course));

});