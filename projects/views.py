from django.shortcuts import render
from projects.models import project 
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from projects.forms import projectModerForm


# Create your views here.
def projectsindex(request):
    allprojects=project.get_all_projects()
    return render(request,"projects/index.html",context={"projects":allprojects})


class projectDetail(DetailView):
    model= project
    template_name= "projects/show.html"

class CreateprojectView(CreateView):
    template_name= "projects/create.html"
    form_class= projectModerForm
    success_url= '/projects/index'

class EditprojectView(UpdateView):
    template_name= "projects/edit.html"
    form_class= projectModerForm
    success_url= '/projects/index'
    model = project
class deletprojectView(DeleteView):
    template_name= "projects/delete.html"
    model = project
    success_url= '/projects/index'
