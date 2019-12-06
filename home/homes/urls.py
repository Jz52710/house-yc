from django.urls import path
from . import views
from .views import Price

urlpatterns=[
    path("",views.index),
    path("api/price",Price.as_view())
]
