from django.urls import path, include

from auth.views import password_change_done

urlpatterns = [
    # path('password/change/done/', password_change_done),
    path('', include('registration.backends.default.urls')),
]