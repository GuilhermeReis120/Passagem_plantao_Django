from django.urls import path
from .views import CustomLoginView, passagem_plantao_view, dashboard_view, passagem_cftv_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', LogoutView.as_view(next_page='login'), name='logout'),
    path('passagem_plantao/', passagem_plantao_view, name='passagem_plantao'),
    path('passagem_cftv/', passagem_cftv_view, name='passagem_cftv'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
