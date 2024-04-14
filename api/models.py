from django.db import models

# Create your models here.
class Todo(models.Model):
    todoName = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.todoName
    
class Item(models.Model):
    itemName = models.CharField(max_length=100)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName


