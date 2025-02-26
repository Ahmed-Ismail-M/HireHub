from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, RegisterEmployeeView, LoginAPI, DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path("api/v1/register/", RegisterEmployeeView.as_view(), name="register"),
    path("api/v1/login/", LoginAPI.as_view(), name="login"),
]