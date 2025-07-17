from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('outbox/', views.outbox, name='outbox'),
    path('send/', views.send_message, name='send'),
    path('message/<int:pk>/', views.view_message, name='view_message'),
]
