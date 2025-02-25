from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def todos_view(request):
    return render(request, "todos/todos.html")