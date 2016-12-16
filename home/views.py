from django.shortcuts import get_object_or_404, render
from projects.models import Projects
from django.http import HttpResponse

def index(request):
    array = Projects.objects.all()
    context = {
        'projects_list': array
    }
    return render(request, 'home/index.html', context)

def about(request):
    return HttpResponse("This is about page")