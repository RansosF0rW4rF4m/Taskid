from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError


# Create your models here.

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    class Meta:
        abstract = True
        managed = True

class User(AbstractUser, ModelBase):
    is_parent = models.BooleanField(default=False)
    is_child = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return f"{self.username} ({'Parent' if self.is_parent else 'Child'})"

    def get_active_tasks(self):
        return self.assigned_tasks.filter(active=True)

class Task(ModelBase):
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('COMPLETED', 'Completa'),
        ('APPROVED', 'Aprovada'),
        ('REJECTED', 'Rejeitada'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey('User', on_delete=models.CASCADE, limit_choices_to={'is_child': True})
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, limit_choices_to={'is_parent': True}, related_name='created_tasks')
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField()