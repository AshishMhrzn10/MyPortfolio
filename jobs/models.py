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


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    