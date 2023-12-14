from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    wallet = models.FloatField(default=0)
    paycheck = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    bought_book = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Users'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Author(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=50)
    keyword = models.CharField(max_length=255, null=True, blank=True)
    des = models.CharField(max_length=255, null=True, blank=True)
    number_of_book = models.BigIntegerField(default=0)
    is_author = models.BooleanField(default=True, editable=False)
    object = models.Manager()

    class Meta:
        db_table = 'Authors'

    def __str__(self):
        return 'stage_name'
