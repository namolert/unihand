// Function to toggle the visibility of appointments
function toggleAppointments() {
  var checkbox = document.getElementById("showAppointments");
  console.log("SOMETHING");
  var appointmentElements = document.querySelectorAll('[data-appointment="true"]');

  // Loop through each appointment and show or hide based on the checkbox
  appointmentElements.forEach(function(element) {
      if (checkbox.checked) {
          element.style.display = "block";  // Show appointment
      } else {
          element.style.display = "none";   // Hide appointment
      }
  });
}

// Ensure appointments are hidden by default when page loads
document.addEventListener("DOMContentLoaded", function() {
  toggleAppointments();  // Call to check initial state
});