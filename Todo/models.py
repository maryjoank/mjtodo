from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = 'Contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'