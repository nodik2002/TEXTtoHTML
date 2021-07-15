from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    body=RichTextField(blank=True,null=True)

class Image(models.Model):
    image = models.ImageField(upload_to='blog_images')
    slug = models.SlugField(max_length = 200,unique=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.image)
        return super().save(*args, **kwargs)