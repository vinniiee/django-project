from django.conf.urls import url
from usermodel_app import views

#TEMPLAE URLS!
app_name ='usermodel_app'


urlpatterns=[
        url(r'^register/$',views.register,name='register'),
        url(r'^user_login/$',views.user_login,name='user_login'),
]
