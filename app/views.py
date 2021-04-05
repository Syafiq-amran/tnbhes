from django.shortcuts import render
from app.models import tblLogs, tblFeederPillars, tblfpsummary
from app.filters import tblLogsFilter, tblfpsummaryFilter
from app.forms import tblLogsForm,tblFeederPillarsForm
from app.serializers import tblLogsSerializer, tblFeederPillarsSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from django import template
from django.contrib.auth.models import Group


register = template.Library() 

#django rest framework api

# @api_view(['GET', 'POST'])
# def logs_list(request, format=None):
#     if request.method == 'GET':
#         test = tblLogs.objects.all()
#         serializer = tblLogsSerializer(test, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = tblLogsSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# class logs_list(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = tblLogs.objects.all()
#     serializer_class = tblLogsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class logs_list(generics.ListAPIView):
    queryset = tblLogs.objects.all()
    serializer_class = tblLogsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['eventname', 'comments']

# Create your views here.
@login_required
def index(request):
    table = tblLogs.objects.all()
    myFilter = tblLogsFilter(request.GET, queryset=table)
    table = myFilter.qs
    return render(request, "index.html", {'table':table, 'myFilter':myFilter})

@login_required
def FeederPillar(request,id):
    # context = {}
    # if request.user.is_superuser:
    #      context['show_tab'] = True
    #      return context
    fd = tblFeederPillars.objects.get(id=id)
    form = tblFeederPillarsForm(instance=fd)
    # group = request.user.groups.values_list('name', flat=True).first()

    return render(request, 'FeederPillar.html', {'fd':fd, 'form':form})


def test_update(request,id):
    pass

def fdview(request):
    view = tblFeederPillars.objects.all()

    return render(request, 'fdview.html', {'view':view})

def test(request):
    return render(request, 'test.html')

def testpage_postget(request):
    return render(request, 'testpage_postget.html')

@login_required
def architecture(request):
    return render(request, 'architecture.html')

@login_required
def feeder_detail(request):
    fpsummary = tblfpsummary.objects.all()
    myFilter = tblfpsummaryFilter(request.GET, queryset=fpsummary)
    fpsummary = myFilter.qs
    return render(request, 'feeder_detail.html', {'fpsummary': fpsummary, 'myFilter':myFilter})

@login_required
def user_manual(request):
    return render(request, 'user_manual.html')

@login_required
def dashboard(request):
    return render(request, 'Dashboard.html')