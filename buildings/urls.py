from django.urls import path

from . import views

app_name = 'buildings'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sort-by/', views.SortDefaultView.as_view(), name='sort-by'),
    path('sort-by/pk/', views.SortPkView.as_view(), name='sort-by-pk'),
    path('sort-by/name/', views.SortNameView.as_view(), name='sort-by-name'),
    path('sort-by/address/', views.SortAdressView.as_view(), name='sort-by-address'),
    path('new/', views.NewBuildingView.as_view(), name='create'),
    path('detail/<int:pk>/', views.DetailBuildingView.as_view(), name='read'),
    path('modify/<int:pk>/', views.ModifyBuildingView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteBuildingView.as_view(), name='delete'),
]
