const loginForm = document.getElementById("login");
const loginButton = document.getElementById("submit");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("I'm clicked!")
    const password = loginForm.password.value.toLowerCase();

    if ( password === "test") {
      alert("Password accepted. Press x to close this and leave through door");
    } else {
      alert("Incorrect password. This door is only for authorized Nomtanso personnel");
    }
})
