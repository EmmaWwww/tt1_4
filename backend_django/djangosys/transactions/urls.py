'''
transactions/
'''
from django.urls import path

from . import views,sign_in_out

urlpatterns = [
    path('orders/', views.listtransactions),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout)
]