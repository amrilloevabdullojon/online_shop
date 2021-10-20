from django.urls import path

from pages.views import AboutView, HomeView, ContactCreateView, LoginView, RegisterView

app_name = 'pages'
urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
]