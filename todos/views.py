from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ToDo
from .forms import ToDoForm

@login_required
def todos_view(request):
    student = request.user.student
    todos = ToDo.objects.filter(student=student).order_by("-created_at")

    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.student = student
            todo.save()
            return redirect("todos")
    else:
        form = ToDoForm()

    context = {
        "todos": todos,
        "form": form,
    }
    return render(request, "todos/todos.html", context)

@login_required
def edit_todo_view(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id, student=request.user.student)

    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todos")
    else:
        form = ToDoForm(instance=todo)

    context = {
        "todos": todo,
        "form": form,
    }
    return render(request, "todos/edit_todo.html", context)

@login_required
def delete_todo_view(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id, student=request.user.student)
    todo.delete()
    return redirect("todos")
