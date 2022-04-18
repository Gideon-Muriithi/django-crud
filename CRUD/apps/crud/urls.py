from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('add', v.add, name='add'),
    path('', v.show, name='show'),
    # path('edit/<int:id>', v.edit, name='edit'),
    path('update/<int:id>', v.update, name='update'),
    path('delete/<int:id>', v.destroy, name='delete'),
]