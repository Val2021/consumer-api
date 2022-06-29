from search_consumer.views import search_data
from django.urls import path

app_name = "search_consumer"
urlpatterns = [
    path('',search_data, name="search_data")
]