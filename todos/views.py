from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem

# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        'todo_lists': todo_lists
    }
    return render(request, 'todos/todo_list_list.html', context)

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_items = TodoItem.objects.filter(list=todo_list)
    context = {
        "todo_list": todo_list,
        "todo_items": todo_items
    }
    return render(request, "todos/todo_list_detail.html", context)

def todo_list_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        todo_list = TodoList(name=name)
        todo_list.save()
        return redirect("todo_list_detail", id=todo_list.id)
    else:
        return render(request, "todos/todo_list_create.html")
