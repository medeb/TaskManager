from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import TaskList,TeamList,TeamMembers
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db.models import Q


class HomePageView(TemplateView):
   
    template_name='TaskAssignment/cards.html'

    def get_context_data(self,**kwargs):
        tasks = TaskList.objects.filter(Q(assignedTo=self.request.user) | Q(assignedBy=self.request.user))
        teams = TeamMembers.objects.filter(team_member=self.request.user)
        
        all_task = tasks.values('team').annotate(Count('task'))#tasks.count()
        pending_task = tasks.filter(status='Pending').values('team').annotate(Count('task'))
        count_list =zip(all_task,pending_task)
        context={
            "tasks" : tasks,
            "teams" : teams,
            "all_task_count":count_list,

        }
        return context

# class DetailTaskView(generic.DetailView):
#     context_object_name = 'all_task'
#     model = TaskList
#     template_name = 'TaskAssignment/taskDetail.html'

def DetailTaskView(request,pk):
    # pk=request.GET.get('id_team')
    if request.method=='POST':
        form_status = request.POST.get('selected_status')
        all_task = TaskList.objects.filter(id=pk).update(status=form_status)
        context={
            'all_task' : all_task
        }
        return redirect(reverse('tasks:home_page'))

    all_task = TaskList.objects.filter(id=pk)
    context={
        'all_task' : all_task
    }
    return render(request,'TaskAssignment/cardDetails.html',context)   
# class CawrdDetialView(generic.ListView):
#     model = TaskList
#     context_object_name = 'all_task'
#     template_name='TaskAssignment/cardDetail.html'
    
#     def get_queryset(self,id_team):
#         # pk=request.get.GET('id_team')      
#         return TaskList.objects.filter(team_id=id_team)

def CardDetialView(request,id_team):
    # pk=request.GET.get('id_team')
    if request.method=='POST':
        form_status = request.GET.get('selected_status')
        all_task = TaskList.objects.filter(id=id_team).update(status=form_status)
        context={
            'all_task' : all_task
        }
        return render(request,'TaskAssignment/cardDetails.html',context)

    all_task = TaskList.objects.filter(team_id=id_team)
    context={
        'all_task' : all_task
    }
    return render(request,'TaskAssignment/cardDetails.html',context)

class CreateTaskView(CreateView):
    model = TaskList
    fields ='__all__'

class CreateTeamView(CreateView):
    model = TeamList
    fields ='__all__'


class AddTeamMemView(CreateView):
    model = TeamMembers
    template_name='TaskAssignment/teamlist_form.html'
    fields='__all__'

class UpdateTaskView(UpdateView):
    model = TaskList
    fields =['status']