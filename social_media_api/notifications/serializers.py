from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  
    target = serializers.SerializerMethodField()  

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'timestamp', 'is_read']

    def get_target(self, obj):
        
        return str(obj.target)