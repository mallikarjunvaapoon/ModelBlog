from django.db import models

class Tags(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return 'Tags[ name: {name}]'.format(name=self.text)

class ModelBlog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tags, related_name='ModelBlog')

    def __str__(self):
        return 'ModelBlog[ name: {name}]'.format( name=self.title)




