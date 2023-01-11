from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class Salary(models.Model):

    name = models.TextField()
    salaryAmount = models.IntegerField()
    currsalaryAmount = models.IntegerField()
    date = models.DateField()

    class Meta:
        verbose_name = ("Salary")
        verbose_name_plural = ("Salarys")

    def __str__(self):
        return self.name


class paid(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.TextField()
    paidAmount = models.IntegerField()
    salary = models.ForeignKey(
        Salary, on_delete=models.CASCADE, related_name='paids')
    date = models.DateField()

    class Meta:
        verbose_name = ("paid")
        verbose_name_plural = ("paids")

    def __str__(self):
        return self.name


@receiver(post_save, sender=get_user_model())
def afterUser(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

    # Create your models here.
