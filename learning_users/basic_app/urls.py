from django.conf.urls import url
from basic_app import views
app_name = "basic_app"
urlpatterns=[
    url(r'^register/$',views.register,name="register"),
    url(regex=r'^login/$', view=views.user_login, name='user_login'),
]
