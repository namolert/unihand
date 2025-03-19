let deleteTodoId = null;

function confirmDelete(todoId) {
  deleteTodoId = todoId;
  document.getElementById("deleteModal").style.display = "flex";
}

function closeModal() {
  document.getElementById("deleteModal").style.display = "none";
}

// Handle delete confirmation
document.addEventListener("DOMContentLoaded", function () {
  const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");

  if (confirmDeleteBtn) {
    confirmDeleteBtn.addEventListener("click", function () {
      if (deleteTodoId) {
        window.location.href = `/todos/delete/${deleteTodoId}/`;
      }
    });
  }
});

// Handle add task confirmation
document.addEventListener('DOMContentLoaded', function() {
  const modal = document.getElementById("addTaskModal");
  const btn = document.getElementById("addTaskBtn_Outside");
  const span = document.getElementsByClassName("close")[0];

  btn.onclick = function() {
    modal.style.display = "block";
    console.log("Something");
  }

  // Close modal when the close button (X) is clicked
  span.onclick = function() {
    modal.style.display = "none"; 
  }

  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
});