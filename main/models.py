from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('ml', 'Machine Learning'),
        ('mobile', 'Mobile'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Languages'),
        ('frameworks', 'Frameworks'),
        ('frontend', 'Frontend'),
        ('databases', 'Databases'),
        ('tools', 'Tools & Platforms'),
        ('concepts', 'Core Concepts'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='languages')

    def __str__(self):
        return self.name




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ['-created_at']
