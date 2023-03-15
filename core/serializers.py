from rest_framework import serializers
from .models import *

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLogin
        fields = '__all__'

class ContentTypeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'

class ContentUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactDetails
        fields = '__all__'