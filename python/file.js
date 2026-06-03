let form = document.getElementById("myForm");
let msg = document.getElementById("msg");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  try {
    let username = document.getElementById("username").value;
    let age = document.getElementById("age").value;

    msg.className = "";

    if (username === "") {
      throw new Error("Username cannot be empty");
    }

    if (username.length < 3) {
      throw new Error("Username must be at least 3 characters");
    }

    if (age === "") {
      throw new Error("Age is required");
    }

    if (age < 18) {
      throw new Error("You must be 18+");
    }

    msg.innerText = "Form submitted successfully ✅";
    msg.classList.add("success");

  } catch (err) {

    msg.innerText = err.message;
    msg.classList.add("error");

  } finally {

    console.log("Validation Attempted");

  }
});
