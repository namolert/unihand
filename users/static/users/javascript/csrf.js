function getCSRFToken() {
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  return csrfToken;
}
