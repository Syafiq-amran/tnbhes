from rest_framework import serializers
from app.models import tblLogs, tblFeederPillars
from app import models

class tblLogsSerializer(serializers.ModelSerializer):
    eventdatetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = tblLogs
        fields =  '__all__'

class tblFeederPillarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblFeederPillars
        fields = '__all__'