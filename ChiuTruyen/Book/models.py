from django.db import models
from User.models import CustomUser, Author
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255, null=True, blank=True)
    des = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    object = models.Manager()

    class Meta:
        db_table = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    alias = models.CharField(max_length=255, null=True, blank=True)
    view = models.BigIntegerField(default=0)
    status_choose = (
        (0, 'Updating'),
        (1, 'Finished'),
        (2, 'Dropped'),
        (3, 'Coming Soon')
    )
    status = models.IntegerField(choices=status_choose, default=0)
    avatar = models.ImageField()
    des = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    keyword = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    object = models.Manager()

    class Meta:
        db_table = 'Books'

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    object = models.Manager()

    class Meta:
        db_table = 'Chapters'

    def __str__(self):
        return self.name


class Pages(models.Model):
    image = models.ImageField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    chapter = models.OneToOneField(Chapter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()

    class Meta:
        db_table = 'Comments'
