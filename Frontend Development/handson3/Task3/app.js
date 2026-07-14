import { courses } from "./data.js";

const grid=document.querySelector(".course-grid");

const search=document.getElementById("search-courses");

const sortBtn=document.getElementById("sort-btn");

const selected=document.getElementById("selected-course");

let displayCourses=[...courses];

// Render Function

function renderCourses(courseList){

grid.innerHTML="";

courseList.forEach(course=>{

const card=document.createElement("article");

card.className="course-card";

card.dataset.id=course.id;

card.innerHTML=`

<h3>${course.name}</h3>

<p>Course Code : ${course.code}</p>

<p>Credits : ${course.credits}</p>

<span>Grade : ${course.grade}</span>

`;

grid.appendChild(card);

});

}

renderCourses(displayCourses);

// Search

search.addEventListener("input",()=>{

const value=search.value.toLowerCase();

const filtered=courses.filter(course=>

course.name.toLowerCase().includes(value)

);

displayCourses=filtered;

renderCourses(displayCourses);

});

// Sort

sortBtn.addEventListener("click",()=>{

displayCourses.sort((a,b)=>b.credits-a.credits);

renderCourses(displayCourses);

});

// Event Delegation

grid.addEventListener("click",(event)=>{

const card=event.target.closest(".course-card");

if(!card) return;

const id=Number(card.dataset.id);

const course=courses.find(c=>c.id===id);

selected.textContent=

`Selected Course : ${course.name} | Grade : ${course.grade}`;

});