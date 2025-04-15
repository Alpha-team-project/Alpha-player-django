from django.urls  import path,include
from  . import views

app_name = 'item'

urlpatterns = [
    path('',views.music_list, name='items'),
    path('<int:pk>/', views.music_detail, name = 'music_detail'),
    path('new/',views.music_new, name='new'),
    path('<int:pk>/delete', views.music_delete, name = 'delete'),
    path('<int:pk>/edit', views.music_edit, name = 'edit'),


     
]
