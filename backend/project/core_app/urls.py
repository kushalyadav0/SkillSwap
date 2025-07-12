from django.urls import path
from .views import register, login, my_profile, public_profiles, create_swap_request, list_my_swaps, update_swap_status

urlpatterns = [
    path('register/', register),
    path('login/', login),

    path('profile/', my_profile),
    path('profile/public/', public_profiles),

    path("swaps/", create_swap_request),              # POST
    path("swaps/list/", list_my_swaps),              # GET
    path("swaps/<int:pk>/status/", update_swap_status),  # PATCH
]
