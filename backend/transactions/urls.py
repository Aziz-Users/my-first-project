from django.urls import path
from .views import *

urlpatterns = [
    path('top-up/',top_up),
    path('postback/', postback),
    path('user-transsactions/', UserTransactions.as_view())
]
