// Course Data

const courses=[

{
id:1,
name:"Data Structures",
code:"CS101",
credits:4
},

{
id:2,
name:"Database Management",
code:"CS102",
credits:3
},

{
id:3,
name:"Operating Systems",
code:"CS103",
credits:4
},

{
id:4,
name:"Computer Networks",
code:"CS104",
credits:3
},

{
id:5,
name:"Web Development",
code:"CS105",
credits:4
}

];

// ----------------------------
// Promise using .then()
// ----------------------------

function fetchUser(id){

fetch("https://jsonplaceholder.typicode.com/users/"+id)

.then(response=>response.json())

.then(user=>{

console.log("User using .then():",user.name);

});

}

fetchUser(1);

// ----------------------------
// async / await
// ----------------------------

async function fetchUserAsync(id){

try{

const response=await fetch(
"https://jsonplaceholder.typicode.com/users/"+id
);

const user=await response.json();

console.log("User using async/await:",user.name);

}

catch(error){

console.log(error);

}

}

fetchUserAsync(2);

// ----------------------------
// Simulate Network Delay
// ----------------------------

function fetchAllCourses(){

return new Promise(resolve=>{

setTimeout(()=>{

resolve(courses);

},1000);

});

}

// ----------------------------
// Render Courses
// ----------------------------

const grid=document.querySelector(".course-grid");

const loading=document.getElementById("loading");

fetchAllCourses()

.then(courseList=>{

loading.style.display="none";

courseList.forEach(course=>{

const card=document.createElement("div");

card.className="course-card";

card.innerHTML=`

<h3>${course.name}</h3>

<p>Course Code : ${course.code}</p>

<span>Credits : ${course.credits}</span>

`;

grid.appendChild(card);

});

});

// ----------------------------
// Promise.all()
// ----------------------------

Promise.all([

fetch("https://jsonplaceholder.typicode.com/users/1").then(r=>r.json()),

fetch("https://jsonplaceholder.typicode.com/users/2").then(r=>r.json())

])

.then(users=>{

console.log("Promise.all Users");

console.log(users[0].name);

console.log(users[1].name);

});