const loading=document.getElementById("loading");

const postsDiv=document.getElementById("posts");

// ---------------------------
// Axios Request Interceptor
// ---------------------------

axios.interceptors.request.use(config=>{

console.log("API call started:",config.url);

return config;

});

// ---------------------------
// Axios apiFetch()
// ---------------------------

async function apiFetch(url){

const response=await axios.get(url,{

params:{
userId:1
}

});

return response.data;

}

// ---------------------------
// Load Posts
// ---------------------------

async function loadPosts(){

loading.style.display="block";

try{

const posts=await apiFetch(
"https://jsonplaceholder.typicode.com/posts"
);

loading.style.display="none";

posts.forEach(post=>{

const card=document.createElement("div");

card.className="post";

card.innerHTML=`

<h3>${post.title}</h3>

<p>${post.body}</p>

`;

postsDiv.appendChild(card);

});

}

catch(error){

loading.textContent="Unable to load posts.";

console.log(error);

}

}

loadPosts();

/*

Difference between Fetch and Axios

1. Fetch does NOT automatically convert JSON.
   Axios automatically converts JSON.

2. Fetch does NOT throw errors for 404 or 500.
   Axios throws errors automatically.

3. Fetch is built into modern browsers.
   Axios is an external library with extra features
   like interceptors, timeout and request cancellation.

*/