const howToButton = document.querySelector(".howto");
const gotchaButton = document.querySelector(".gotcha");
const howToContainer = document.querySelector(".secondary-container");
const mainContainer = document.querySelector(".display-container");

howToContainer.classList.add("hidden");
howToButton.addEventListener('click', ()=>{
    howToContainer.classList.remove("hidden")
    mainContainer.classList.add("hidden")
})
gotchaButton.addEventListener('click',()=>{
    mainContainer.classList.remove("hidden")
    howToContainer.classList.add("hidden")
})
