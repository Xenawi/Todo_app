from django.db import models

class TODO(models.Model):
    todo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    date_of_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
