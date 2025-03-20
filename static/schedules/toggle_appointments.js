function toggleAppointments() {
  const checkBox = document.getElementById("showAppointments");
  const appointmentRows = document.querySelectorAll(".appointments");

  appointmentRows.forEach((row) => {
    row.style.display = checkBox.checked ? "table-row" : "none";
  });
}
