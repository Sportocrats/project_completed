
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('main1.html', views.main1, name='main1'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('announce.html', views.announce, name='announce'),
    path('contactus.html', views.contactus, name='contactus'),
    path('register.html', views.register, name='register'),
    path('male.html', views.male, name='male'),
    path('female.html', views.female, name='female'),
    path('screening.html', views.screening, name='screening'),
    path('trial_male.html', views.trial_male, name='trial_male'),
    path('trial_female.html', views.trial_female, name='trial_female'),
    path('final_male.html', views.final_male, name='final_male'),
    path('final_female.html', views.final_female, name='final_female'),

]