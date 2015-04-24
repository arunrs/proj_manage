from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class DateInfoModel(models.Model):

    """
    This is Abstract model. it used for
    inhertiance
    """

    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PeriodInfoModel(models.Model):

    start_date = models.DateField(null=True, blank=True)
    end_date =  models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

        
class InfoModel(DateInfoModel):

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True


class CommonInfoModel(InfoModel, PeriodInfoModel):

    class Meta:
        abstract = True


class Modelreference(DateInfoModel):

    model_name = models.CharField(max_length=50)
    reference = models.IntegerField()

    class Meta:
        abstract = True        


class Domian(InfoModel):
    
    def __str__(self):
        return self.name


class ProjectMeta(models.Model):

    team_name = models.CharField(max_length=150)

    developer = models.ManyToManyField(User,
                                       related_name=_("project_developer"),
                                       verbose_name=_("project_developer"))
    scrum = models.ForeignKey(User,
                              related_name=_("project_scrum"),
                              verbose_name=_("project_scrum"))
    
    project_watcher = models.ManyToManyField(User,
                                             related_name=_("watchers"),
                                             verbose_name=_("watchers"))


    def __str__(self):

        return self.team_name
    
    
    
class Project(CommonInfoModel):

    client_name = models.ForeignKey(User,
                                    related_name=_("client_name"),
                                    verbose_name=_("client_name"))
    domain = models.ForeignKey(Domian,
                              related_name=_("project_domain"),
                              verbose_name=_("project_domain"))

    meta = models.ForeignKey(ProjectMeta,
                             related_name=_("project_meta"),
                             verbose_name=_("project_meta"))

    class Meta:

        db_table = 'project'
        
        
    def __str__(self):

        return self.name


class Sprint(CommonInfoModel):

    version = models.FloatField(default=0.1)
    tagged = models.FloatField(null=True, blank=True)
    project_ref = models.ForeignKey(Project,
                                    related_name=_("project_ref"),
                                    verbose_name=_("project_ref"))
    freezed_sprint = models.BooleanField(default=True)


    class Meta:

        db_table = "sprint"
        unique_together = ("project_ref", "name")
        
        
    def __str__(self):

        return self.project_ref.name + "-" + self.name



class FilereferenceModel(Modelreference):

    image_file = models.ImageField()
    
    class Meta:
        db_table = 'file_paths'


class CommentModel(Modelreference):

    comment = models.TextField()

    class meta:

       db_table = 'comments'


class CommonTaskInfo(CommonInfoModel):

    CHOICES = (('C', 'Current'),
               ('E', 'Enhancement'))

    STATUS = (('N', 'New'),
              ('O', 'Open'),
              ('C', 'Closed'))
                
    types = models.CharField(max_length=1,
                             choices=CHOICES,
                             default='C')

    status = models.CharField(max_length=1,
                              choices=STATUS,
                              default='N')

    closed = models.BooleanField(default=False)

    reopened = models.IntegerField(default=0)

    class Meta:

        abstract = True
                

    
class Task(CommonTaskInfo):

    
    technology = models.CharField(max_length=100)
    
    sprint = models.ForeignKey(Sprint,
                               related_name=_("sprint_name"),
                               verbose_name=_("sprint_name"))
    
    allocated_user = models.ForeignKey(User,
                                       related_name=_("alloted_dev"),
                                       verbose_name=_("alloted_dev")
                                       )
    slug_name = models.SlugField(null=True, blank=True)

    screeshots = models.ForeignKey(FilereferenceModel,
                                   null=True,
                                   blank=True,
                                   limit_choices_to={"model_name":"Task"})
    
    estimated_hrs = models.PositiveSmallIntegerField(default=1)
    
    any_delay = models.BooleanField(default=True)
    
    reason_delay = models.TextField(null=True, blank=True)
    
    comments = models.ForeignKey(CommentModel,
                                null=True,
                                blank=True,
                                limit_choices_to={"model_name": "Task"})
    
    additional = models.BooleanField(default=False)

    class Meta:
        db_table = 'task'
    

    def __str__(self):

        return self.slug_name
        
    def save(self, *args, **kwargs):

        print(dir(self))

        #self.slug_name = self.sprint.__name__ + " " + self.name

        return super(Task, self).save(*args, **kwargs)

    
class Bug(CommonTaskInfo):

    page_url = models.URLField(null=True,
                               blank=True)

    screenshot = models.ForeignKey(FilereferenceModel,
                                   null=True,
                                   blank=True,
                                   limit_choices_to={"model_name":"Bug"})
    
    comments = models.ForeignKey(CommentModel,
                                null=True,
                                blank=True,
                                limit_choices_to={"model_name": "Bug"})
    
    related_task = models.ForeignKey(Task,
                                     null=True,
                                     blank=True
                                     )
    class Meta:

        db_table = 'bug'


    def __str__(self):

        return self.name
