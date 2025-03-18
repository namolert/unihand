function loginUser(event) {
  event.preventDefault();

  const formData = new FormData(document.getElementById("loginForm"));
  const data = {
    username: formData.get("username"),
    password: formData.get("password"),
  };

  fetch("/api/users/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken(),
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.token) {
        window.location.href = "home/";
      } else {
        alert("Login failed: " + JSON.stringify(data));
      }
    })
    .catch((error) => console.error("Error:", error));
}
