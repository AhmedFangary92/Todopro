from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('submit', views.submit, name='submit'),
    path('sortdata', views.sortdata, name='sortdata'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('searchdata', views.searchdata, name='searchdata'),
    path('update/<int:id>', views.update, name='update')
]
