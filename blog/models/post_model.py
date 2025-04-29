from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

from . import author_model, tag_model

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", null=True)
    date = models.DateField(auto_now=True) # More
    slug = models.SlugField(unique=True) # More
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(author_model.Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(tag_model.Tag)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.title}"