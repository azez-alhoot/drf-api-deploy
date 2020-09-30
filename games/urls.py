from django.urls import path

from .views import GameDetails, GamesList

urlpatterns = [
    path('', GamesList.as_view(), name='games'),
    path('/<int:pk>', GameDetails.as_view(), name='game_details'),
]