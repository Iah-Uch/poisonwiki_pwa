from django.urls import path
from . import views

app_name = "poisons"

urlpatterns = [
    path("", views.PoisonListView.as_view(), name="list"),
    # path("add/", views.EventCreateView.as_view(), name="add"),
    # path("history/", views.EventHistoryListView.as_view(), name="history"),
    path("<int:pk>/", views.PoisonDetailView.as_view(), name="detail"),
    # path("<int:pk>/update", views.EventUpdateView.as_view(), name="update"),
    # path("<int:pk>/delete", views.EventDeleteView.as_view(), name="delete"),
]