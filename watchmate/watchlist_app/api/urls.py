from django.contrib import admin
from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import ReviewDetail ,ReviewList ,WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('stream/<int:pk>/reviews', ReviewList.as_view(), name='review-list'),
    
]
