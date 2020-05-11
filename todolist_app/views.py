#todolist_app\views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method== "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            #form.save(commit=False).owner = request.user
            #form.save()
            #atau
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        messages.success(request,("Kegitan baru ditambahkan!"))
        return redirect('todolist')
    else:
        #all_task = TaskList.objects.all() --jik menampilkan semua data siapa aja
        all_task = TaskList.objects.filter(owner=request.user).order_by('id').reverse()
        page = request.GET.get('page', 1)
        paginator = Paginator(all_task, 10)
        try:
            all_tasks = paginator.page(page)
        except PageNotAnInteger:
            all_tasks = paginator.page(1)
        except EmptyPage:
            all_tasks = paginator.page(paginator.num_pages)

        return render(request, 'todolist.html', { 'all_tasks': all_tasks })

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, ("Akses dilarang, Anda tidak diperbolehkan"))

    return redirect('todolist')
    
@login_required
def edit_task(request, task_id):
    if request.method== "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,("Kegiatan berhasil di edit!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)

        return render(request, 'edit.html',{'task_obj': task_obj })

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Akses dilarang, Anda tidak diperbolehkan"))
    
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ("Akses dilarang, Anda tidak diperbolehkan"))
        
    return redirect('todolist')

def contact(request):
    context ={
        'contact_text' : "Selamat datang di halaman kontak",
    }
    return render(request, 'contact.html', context)

def about(request):
    context ={
        'about_text' : "Merupakan aplikasi yang bisa anda gunakan untuk merencanakan dan memonitor kegiatan harian. Sangat membantu untuk perencanaan yang baik bagi kehidupan Anda. Silahkan menggunakan",
    }
    return render(request, 'about.html', context)

def index(request):
    context ={
        'index_text' : "Welcome to Index Page",
    }
    return render(request, 'index.html', context)
