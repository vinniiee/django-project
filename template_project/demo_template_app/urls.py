from django.conf.urls import url
from . import views #from current app



#TEMPLATE TAGGING
app_name = 'demo_template_app'

urlpatterns = [

        url(r'^relative/$',views.relative,name='relative'),
        url(r'^other/$',views.other,name='other'),

]
