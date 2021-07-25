from django.urls import path
from . import views

app_name= 'my_vacation'
urlpatterns = [
    path('', views.VacationList.as_view(), name='index'),
    path('my-vacation/<int:pk>/', views.MyVacation.as_view(), name='my_vacation'),
    path('detail/<int:pk>/', views.VacationDetail.as_view(), name='detail'),
    path('edit/<int:pk>/', views.EditVacation.as_view(), name='edit'),
    path('create/', views.CreateVacation.as_view(), name='create'),
    path('search/', views.SearchVacation.as_view(), name='search'),
    path('search/my-vacation', views.SearchMyVacation.as_view(), name='search_my_vacation'),
    path('delete/<int:pk>/', views.DeleteVacation.as_view(), name='delete'),
    path('delete/nonauthority_delete/', views.NonAuthorityDeleteVacation.as_view(), name='nonauthority_delete'),
    path('duplicate/', views.DuplicateVacation.as_view(), name='duplicate'),
]