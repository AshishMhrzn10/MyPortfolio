from django.db import models

# Create your models here.
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"
    
    def __str__(self):
        return "About Me"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work Title")
    image = models.ImageField(upload_to='works/')

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Clent say") 
    image = models.ImageField(upload_to='clents/', default="default.png")

    def __str__(self):
        return self.name
    
    