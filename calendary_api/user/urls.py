from django.urls import path
from .views import TokenView
# from .views import ExpirationTokenAuthentication
from .views import UserInfoView

urlpatterns = [
    path('token/', TokenView.as_view()),
    # path('check/', ExpirationTokenAuthentication),
    path('check_user/', UserInfoView.as_view())
]
