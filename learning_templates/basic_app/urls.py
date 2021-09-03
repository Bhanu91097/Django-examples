from basic_app import views
from django.conf.urls import url

#TEMPLATE TAGGING
app_name = 'basic_app'      #globally declaring the basic_app to app_name

urlpatterns = [
    url(r'^relative/',views.relative,name='relative'),
    url(r'^other/',views.other,name='other')
]
