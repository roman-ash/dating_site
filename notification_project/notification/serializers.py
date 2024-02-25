from rest_framework import serializers
from .models import Client, Newsletter, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
    #matchingKey = serializers.SerializerMethodField()
    #date = MessageSerializer(many=True)
    class Meta:
        model = Newsletter
        fields = '__all__'
        #fields = ('id', 'start_date', 'text', 'end_date', 'message_set')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
