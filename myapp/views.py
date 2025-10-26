from django.shortcuts import get_object_or_404, render, redirect
from .forms import TODOForm
from .models import TODO
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_view')
def index(request):
    return render(request, 'myapp/index.html')


# -------------CRUD------------#
# -----------------------------#
# -----------------------------#

# -----------CREATE------------
@login_required(login_url='login_view')
def add_todo(request):
    form = TODOForm()
    if request.method == 'POST':
        form = TODOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request, 'myapp/add_todo.html', {'form': form})


# ----------------READ-------------

@login_required(login_url='login_view')
def todo_list(request):
    todos = TODO.objects.all()
    return render(request, 'myapp/todo_list.html', {'todos': todos})

# --------------UPDATE---------------
@login_required(login_url='login_view')
def todo_update(request, todo_id):
    todos = TODO.objects.get(todo_id=todo_id)
    if request.method == 'POST':
        form = TODOForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
            return redirect(todo_list)
    else:
        form = TODOForm(instance=todos)
    return render(request, 'myapp/add_todo.html', {'form':form})

# -----------------DELETE--------------
@login_required(login_url='login_view')
def todo_delete(request, todo_id):
    todo = TODO.objects.get(todo_id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect (todo_list)
    return render(request, 'myapp/confirm_delete.html', {'todo':todo})

@login_required(login_url='login_view')
def toggle_done(request, todo_id):
    todo = get_object_or_404(TODO, todo_id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')