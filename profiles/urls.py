from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    path('', login_required(ProfileListView.as_view()), name='list'),
    path('<username>/', login_required(ProfileDetailView.as_view()), name='detail'),
], "profiles")
