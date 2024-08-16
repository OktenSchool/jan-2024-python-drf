from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import ActiveUserView, RecoverPasswordView, RecoveryPasswordRequestView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActiveUserView.as_view()),
    path('/recovery', RecoveryPasswordRequestView.as_view()),
    path('/recovery/<str:token>', RecoverPasswordView.as_view()),

]
