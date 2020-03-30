from django.db import models

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, db_column = 'name')
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name