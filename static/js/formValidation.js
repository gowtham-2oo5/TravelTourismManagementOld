function validateForm() {
  var name = document.getElementById("name").value;
  var age = document.getElementById("age").value;
  var gender = document.getElementById("gender").value;
  var username = document.getElementById("username").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  if (name == "") {
    alert("Please enter your name");
    return false;
  }

  if (age == "") {
    alert("Please enter your age");
    return false;
  }

  if (gender == "") {
    alert("Please select your gender");
    return false;
  }

  if (username == "") {
    alert("Please enter your username");
    return false;
  }

  if (email == "") {
    alert("Please enter your email");
    return false;
  }

  if (password == "") {
    alert("Please enter your password");
    return false;
  }

  return true;
}
