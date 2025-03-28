from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tos/', views.tos, name='tos'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('faq/', views.faq, name='faq'),
    path('ship/<int:ship_id>/', views.ship_detail_view, name='ship_detail'),
    path('add_to_rental/<int:ship_id>/', views.add_to_rental, name='add_to_rental'),
    path('profile/', views.get_profile, name='profile'),
]