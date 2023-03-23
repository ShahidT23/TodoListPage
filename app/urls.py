from django.contrib import admin
from django.urls import path 
from . import views

app_name="app"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.homepage , name ="homepage"),
    path('add', views.add_todo , name ="add_todo"),
    path('delete/<id>',views.delete_todo , name="delete_todo"),
    path('update/<id>',views.update_todo ,name="update_todo")

]