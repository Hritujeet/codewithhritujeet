from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to='courses/images', default="")
    about = models.TextField()

class Tutorial(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=600)
    content = models.TextField()
    course = models.CharField(max_length=500)
    timestamp = models.DateField()

    def __str__(self) -> str:
        return f"Tutorial {self.title} from Course {self.course}"
    
