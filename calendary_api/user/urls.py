from django.urls import path
from .views import LoginView
# from .views import ExpirationTokenAuthentication
from .views import UserInfoView
from .views import SignUpViewSet
from .views import LogoutViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user/signup', SignUpViewSet)
# router.register(r'check_user', UserInfoView)
urlpatterns = [
    path('user/login/', LoginView.as_view()),
    # path('check/', ExpirationTokenAuthentication),
    #path('user/signup/', SignUpView.as_view()),
    path('check_user/', UserInfoView.as_view()),
    path('user/logout/', LogoutViewSet.as_view())
]

urlpatterns += router.urls