from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    code=models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=2, choices=[('S', 'S'), ('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('E','E')],default='E')
    credit = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code} subject Name: {self.name} - Grade: {self.grade}, Credit: {self.credit}"
