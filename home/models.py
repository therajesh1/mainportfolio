from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    msg=models.TextField()

    def __str__(self):
        return self.name