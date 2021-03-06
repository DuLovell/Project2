from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listings/<int:id>", views.advertisement, name="advertisement"),
    path("accounts/<str:username>", views.profile, name="profile"),
    path("watchlist", views.watchlist, name="watchlist")
]

