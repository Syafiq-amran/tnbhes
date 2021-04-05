import django_filters
from django_filters import IsoDateTimeFilter, CharFilter
from django import forms
from app.models import tblLogs, tblfpsummary

class tblLogsFilter(django_filters.FilterSet):
    startdate = IsoDateTimeFilter(field_name="eventdatetime",  lookup_expr='gte')
    enddate = IsoDateTimeFilter(field_name="eventdatetime", lookup_expr='lte') 
    eventname = CharFilter(field_name="eventname", lookup_expr="icontains")
    description = CharFilter(field_name="description", lookup_expr="icontains")
    filepathname = CharFilter(field_name="filepathname", lookup_expr="icontains")
    transfduration = CharFilter(field_name="transfduration", lookup_expr="icontains")
    tohost = CharFilter(field_name="tohost", lookup_expr="icontains")
    fromhost = CharFilter(field_name="fromhost", lookup_expr="icontains")

    class Meta:
        model=tblLogs
        fields = '__all__'

class tblfpsummaryFilter(django_filters.FilterSet):
    fpstatus = django_filters.CharFilter(lookup_expr='icontains')
    fplocation = django_filters.CharFilter(lookup_expr='icontains')
    fpsn = django_filters.CharFilter(lookup_expr='icontains')
    fpipaddr = django_filters.CharFilter(lookup_expr='icontains')
    fprating = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = tblfpsummary
        fields = '__all__'
    
