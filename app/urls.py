from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('index/', views.index,name='index'),  #Home site
    path('FeederPillar/<int:id>', views.FeederPillar, name='FeederPillar'),
    path('fdview/', views.fdview, name='fdview'),
    path('test_update/<int:id>', views.test_update),
    path('logs_list/', views.logs_list.as_view(), name='logs_list'),
    path('test/', views.test, name='test'),
    path('testpage_postget/', views.testpage_postget, name='testpage_postget'),
    path('', auth_views.LoginView.as_view(), name='registration/login'),
    path('accounts/', include('django.contrib.auth.urls')), #new add
    path('architecture/', views.architecture, name="architecture"),
    path('feeder_detail/', views.feeder_detail, name="feeder_detail"),
    path('user_manual/', views.user_manual, name="user_manual"),
    path('Dashboard/', views.dashboard, name="Dashboard")
    # path('logs_detail/<pk>', views.logs_detail, name='logs_detail'),
]
