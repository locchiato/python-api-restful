from django.urls import path

from professors.views import detail
from professors.views import update
from professors.views import index
from professors.views import create
from professors.views import delete

app_name = 'professors'

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
    path('<int:pk>/update', update, name='update'),
    path('<int:pk>/delete', delete, name='delete'),
]
