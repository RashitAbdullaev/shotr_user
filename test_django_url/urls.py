from django.urls import path
from .views import UrlView, MyProjectLoginView, RegisterUserView, CreateUrl,AddJsonApi,MyUserLogout

urlpatterns = [
    path('', UrlView.as_view(), name="short_url"),
    path('login/', MyProjectLoginView.as_view(), name="login"),
    path('register/', RegisterUserView.as_view(), name="register"),
    path('create_url/', CreateUrl.as_view(), name='create_url'),
    path('add_json', AddJsonApi.as_view(), name='add_json'),
    path('logout', MyUserLogout.as_view(), name='logout_url'),

]
