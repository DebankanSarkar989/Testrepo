from django.urls import path
from core.views import index

app_name ="baurl"

urlpatterns=[
    path("baurl/",views.index)
]