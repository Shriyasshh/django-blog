from django.db import models

# Create your models here.

class About(models.Model):
    about_heading = models.CharField(max_length = 20)
    about_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_heading
    
    class Meta:
        verbose_name_plural = 'About'

class SocialLinks(models.Model):
    platform = models.CharField(max_length=20)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform
    class Meta:
        verbose_name_plural = 'Social Links'