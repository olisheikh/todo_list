from django.urls import path
from m.views import home_view, add_task_view

urlpatterns = [
    path('', home_view, name='home'),
    path('add_task/', add_task_view, name='add_task')
]