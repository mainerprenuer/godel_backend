from django.contrib import admin
from django.urls import path
# from rest_framework import views
from api import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('popular/',views.popularview,name='popularview' ),
    path('popularlist/',views.popularlistview,name='popularlistview' ),
    path('recommended/',views.recommendedview,name='recommendedview' ),
    path('recommendedlist/',views.recommendedlistview,name='recommendedlistview' ),
    path('img/',views.imgsnd,name='imgsnd' ),
    path('popular/<int:id>/', views.fetchpopular ,name='popular'),
    path('recommended/<int:id>/', views.fetchrecommended ,name='recommended'),

    path('users/',views.adduser,name='usercrud' ),
    path('login/',views.login,name='logincrud' ),
    path('cart/',views.addcart,name='addcart' ),
    path('fetchcart/',views.fetchcart,name='getcart' ),
    path('deletecart/',views.deletecart,name='deletecart' ),
    path('addfav/',views.addfav,name='addfav' ),

]


urlpatterns+=staticfiles_urlpatterns()



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.getRoutes),
#     path('popular/', views.getPopular),
#     path('popular/<str:pk>/', views.getPopular),

#     path('recommended/', views.getRecommended)
# ]