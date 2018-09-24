from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class TeamList(models.Model):
    name = models.CharField(unique=True,max_length=50)
    description = models.CharField(max_length=120)
    def get_absolute_url(self): 
        return reverse('tasks:team_members',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
    #member = models.ForeignKey(User,on_delete=CASCADE)


# class Report(models.Model):
#     user_id = models.ForeignKey(User, related_name="task_submittedBy")
#     task_id = models.ManyToManyField(TaskList)

class TaskList(models.Model):
    team =  models.ForeignKey(TeamList,on_delete=models.CASCADE)
    task = models.CharField(max_length=30)
    assign_date = models.DateField(auto_now=False, auto_now_add=True)
    assignedBy = models.ForeignKey(User, related_name="task_assignedBy")
    assignedTo = models.ForeignKey(User, related_name="task_assignedTo")
    # currentStauts =  models.IntegerField()
    STATUS_CHOICES = (
        ('Pending'  ,'Pending'),
        ('Started'  ,'Started'),
        ('Completed','Completed')
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending',
        blank=True,
    )
    
    def get_absolute_url(self): #use cases>?
        return reverse('tasks:home_page')

    def __str__(self):
        return self.task

class TeamMembers(models.Model):
    team_name = models.ForeignKey(TeamList,on_delete=models.CASCADE)
    team_member = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team_name)

    def get_absolute_url(self): 
        return reverse('tasks:team_members',kwargs={'pk':self.pk})

    