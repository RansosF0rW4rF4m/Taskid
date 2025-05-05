import rest_framework
from rest_framework import serializers

from core.models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'is_child',
                  'is_parent',
                  'parent',
                  'first_name',
                  'last_name',
                  'username',
                  'email',
                  'password',
                  'created_at',
                  'modified_at',
                  'active',
                  )
        extra_kwargs = {'password': {'write_only': True}, 'created_at': {'read_only': True}, 'modified_at': {'read_only': True}}



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'title',
                  'description',
                  'status',
                  'assigned_to',
                  'created_by',
                  'due_date',
                  'created_at',
                  'modified_at',
                  'active',
                  )