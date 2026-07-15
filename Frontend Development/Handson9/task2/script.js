const cards = document.querySelectorAll(".course-card");

cards.forEach(card => {

card.addEventListener("click", () => {

alert(card.querySelector("h3").textContent);

});

card.addEventListener("keydown", (event) => {

if(event.key==="Enter"){

alert(card.querySelector("h3").textContent);

}

});

});