from django.urls import path

from .views import index, sign_in_step_one, sign_in_step_two


urlpatterns = [
    path('', index),
    path('sign_in', sign_in_step_one),
    path('vk-auth', sign_in_step_two),
]
