function registerUser(event) {
  event.preventDefault();

  const formData = new FormData(document.getElementById("registerForm"));
  const data = {
    username: formData.get("username"),
    email: formData.get("email"),
    password: formData.get("password"),
    password2: formData.get("password2"),
  };

  fetch("/api/users/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Registration successful!");
      } else {
        alert("Error: " + JSON.stringify(data));
      }
    })
    .catch((error) => console.error("Error:", error));
}
