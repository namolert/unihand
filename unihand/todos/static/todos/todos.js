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
