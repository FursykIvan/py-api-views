from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreAPIView, ActorGenericAPIView, CinemaHallViewSet, MovieModelViewSet

app_name = "cinema"

router = DefaultRouter()
router.register("movies", MovieModelViewSet, basename="movies")

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list",
             "post": "create"},
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={"get": "retrieve",
             "put": "update",
             "patch": "partial_update",
             "delete": "destroy"},
)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreAPIView.as_view(), name="genre-detail"),
    path("actors/", ActorGenericAPIView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorGenericAPIView.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
]
