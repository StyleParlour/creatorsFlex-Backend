from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home , name="home"),
    path('signup/', views.signupView , name="signupView"),
    path('uploadContent/', views.uploadContent , name="uploadContent"),
    path('addSocialLogin/', views.addSocialLogin , name="addSocialLogin"),
    path('contact/', views.contact , name="contact"),
     path('api-auth/', include('rest_framework.urls')),
]
