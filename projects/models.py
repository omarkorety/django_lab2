from django.db import models
from django.shortcuts import reverse
# Create your models here.


class project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    time = models.IntegerField(default=10)
# Create your models here.
    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_projects(cls):
        return cls.objects.all()
    

    def get_show_url(self):
        return reverse("projects.show",args=[self.id])


    def get_edit_url(self):
        # return reverse("projects.edit",kwargs={"pk":self.id})
        return reverse("projects.edit", kwargs={"pk":self.id})


    def get_delete_url(self):
        return reverse("projects.delete",args=[self.id])
        # return reverse("projects.delete", kwargs={"id":self.id})
