from django.urls import path,include
from rest_framework import routers
from . import views

app_name = 'giveaway'
urlpatterns = [
    # path('', include(router.urls)),
    # path('answer-url', views.scso, name='scso'),
    path('', views.index, name='index'),
    path('register/<str:session_key>', views.register, name='register'),
    path('fail/<str:message>', views.fail, name='fail'),
    path('success/<str:message>', views.success, name='success'),
    # path('<int:roll_id>/direct/', views.direct, name='direct')
]
