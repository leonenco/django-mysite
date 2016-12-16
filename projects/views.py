from django.shortcuts import get_object_or_404, render
from .models import Projects


def index(request):
    array = Projects.objects.all()
    context = {
        'projects_list': array
    }
    return render(request, 'projects/index.html', context)

def project(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    context = {
        'project': project
    }
    return render(request, 'projects/project-desc.html', context)