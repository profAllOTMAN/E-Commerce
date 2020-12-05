from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing",views.creat_listing,name="create_listing"),
    path("page_listing",views.page_listing,name="page_listing")
    
]


"""

    path("active_listing",views.active_listing,name="active_listing"),
"""