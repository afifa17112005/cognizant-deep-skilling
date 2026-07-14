const loading = document.getElementById("loading");

const notificationList = document.getElementById("notification-list");

const errorDiv = document.getElementById("error");

const retryBtn = document.getElementById("retryBtn");

// ----------------------------
// Reusable Fetch Function
// ----------------------------

async function apiFetch(url){

const response = await fetch(url);

if(!response.ok){

throw new Error("Failed to fetch data. Status : " + response.status);

}

return await response.json();

}

// ----------------------------
// Load Notifications
// ----------------------------

async function loadNotifications(){

loading.style.display="block";

notificationList.innerHTML="";

errorDiv.textContent="";

retryBtn.style.display="none";

try{

// Change the URL below to "/nonexistent"
// to test the error handling.

const posts = await apiFetch(
"https://jsonplaceholder.typicode.com/posts?_limit=6"
);

loading.style.display="none";

posts.forEach(post=>{

const card=document.createElement("div");

card.className="notification";

card.innerHTML=`

<h3>${post.title}</h3>

<p>${post.body}</p>

`;

notificationList.appendChild(card);

});

}

catch(error){

loading.style.display="none";

errorDiv.textContent="Unable to load notifications.";

retryBtn.style.display="block";

console.log(error);

}

}

// ----------------------------
// Retry Button
// ----------------------------

retryBtn.addEventListener("click",loadNotifications);

// ----------------------------
// Initial Load
// ----------------------------

loadNotifications();