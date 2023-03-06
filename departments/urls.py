from django.urls import path

from departments.views import detail
from departments.views import update
from departments.views import index
from departments.views import create
from departments.views import delete

app_name = 'departments'

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
    path('<int:pk>/update', update, name='update'),
    path('<int:pk>/delete', delete, name='delete'),
]
