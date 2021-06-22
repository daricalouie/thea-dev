const loginForm = document.getElementById("login");
const loginButton = document.getElementById("submit");
const loginPanel = document.getElementById("panel");
const donePanel = document.getElementById("done");


loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("I'm clicked!")
    const password = loginForm.password.value.toLowerCase();

    if ( password === "test") {
        donePanel.style.display ='block';
        loginPanel.style.display = 'hidden';
    } else {
      alert("Incorrect password. This door is only for authorized Nomtanso personnel");
    }
})
