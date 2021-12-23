from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddLaptopView.as_view(), name='add_lap'),
    path('show/', views.ShowLaptopView.as_view(), name='show_lap'),
    path('delete/<int:i>', views.DeleteLaptopView.as_view(), name='delete'),
    path('update/<int:i>', views.UpdateLaptopView.as_view(), name='update'),

]