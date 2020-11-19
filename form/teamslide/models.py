from django.db import models

# Create your models here.
class MemberName(models.Model):
    member_name = models.CharField(max_length=100)
    def __str__(self):
        return self.member_name