const loginForm = document.getElementById("login");
const loginButton = document.getElementById("submit");
const loginPanel = document.getElementById("panel");
const donePanel = document.getElementById("done");
const wrongPanel = document.getElementById("wrong");


loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("I'm clicked!")
    const password = loginForm.password.value.toLowerCase();

    if ( password === "test") {
        donePanel.style.display ='block';
        loginPanel.style.display = 'none';
        wrongPanel.style.display = 'none';
        fetch("https://gather.town/api/getMap?spaceId=bLC4E96xZ4dVKnTF\\testing&apiKey=doa91a6eaEZV6r5P&mapId=empty-room-small-brick").then(function (response) {
    return response.json();
  })
    } else {
      wrongPanel.style.display = 'block';
    }
})
