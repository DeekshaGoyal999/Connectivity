from django.urls import path
from posts.views import (
    home_view,
    post_detail_view,
    post_list_view,
    post_create_view,
    post_delete_view
    )
urlpatterns = [
    path('p/', home_view),
    path('p/<int:post_id>', post_detail_view),
    path('p/all', post_list_view),
    path('p/create', post_create_view),
    path('p/<int:post_id>/delete', post_delete_view),
]