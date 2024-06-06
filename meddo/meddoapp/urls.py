from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, TripCreateView, TripDetailView, TripListView, SignUpView

app_name = 'meddoapp'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('create_trip',TripCreateView.as_view(),name='create_trip'),
    path('detail_trip/<int:pk>/',TripDetailView.as_view(),name='detail_trip'),
    path('list_trip',TripListView.as_view(),name='list_trip'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='meddoapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
