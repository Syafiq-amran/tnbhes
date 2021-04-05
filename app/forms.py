from django import forms
from app.models import tblLogs,tblFeederPillars

class tblLogsForm(forms.ModelForm):
    class Meta:
        model=tblLogs
        fields = '__all__'

class tblFeederPillarsForm(forms.ModelForm):
    class Meta:
        model = tblFeederPillars
        fields = '__all__'