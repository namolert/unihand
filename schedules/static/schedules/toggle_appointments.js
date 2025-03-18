function toggleAppointments() {
  // Get all schedule rows
  const checkBox = document.getElementById("showAppointments");

  // Iterate through all course schedules and toggle the appointments display
  const scheduleIds = document.querySelectorAll(".schedule-row");
  scheduleIds.forEach((row) => {
    const appointmentsDiv = row.querySelector(".appointments");
    // Toggle display based on checkbox state
    if (checkBox.checked) {
      appointmentsDiv.style.display = "block";
    } else {
      appointmentsDiv.style.display = "none";
    }
  });
}
