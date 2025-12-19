from django.shortcuts import render, redirect
from .forms import TaskForm
# Create your views here.

def home_view(request):
    return render(request, 'home.html', {})

def add_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form':form})

