from django.urls import path
from bookingapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('contact.html',views.contact,name='contact'),
    path('driver.html',views.driver,name='driver'),
    path('details/',views.bookingdetails,name='details'),
    path('driverdetails/',views.driverdetails,name='driverdetails'),
    path('login/',views.loginform,name='login'),
    path('logout/',views.logoutform,name='logout'),
]
