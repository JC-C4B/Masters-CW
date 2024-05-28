
// Setting our API URL to a variable for easy access
url = "https://api.adviceslip.com/advice"

// Telling our HTML doc what to do when our button is clicked
document.getElementById("Submit").addEventListener("click", handleClick);

// Defining our function to return the '.advice' information from our API
function handleClick() {
    fetch(url)
    .then(response => response.json())
    .then(data => {
        advice = data.slip.advice;
        document.querySelector(".advice").textContent = advice;
    })
}





