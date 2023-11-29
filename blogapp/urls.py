from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('<int:pk>', views.BlogDetail.as_view(), name='blog_detail'),
]

