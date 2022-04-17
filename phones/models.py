from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    image = models.URLField(default=None)
    price = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(default=None, max_length=40)


    def __str__(self):
        return f'{self.id}, {self.name}'


