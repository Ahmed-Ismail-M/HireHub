from hirehub.serializers.emp_serializer import RegisterEmployeeSerializer, EmployeeLoginSerializer, EmployeeSerializer
from hirehub.serializers.serializers import CompanySerializer, DepartmentSerializer
from hirehub.models import Company, Department, Employee
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from hirehub.mw import auth_required, allowed_users
from django.db import transaction


class RegisterEmployeeView(generics.CreateAPIView):
    serializer_class = RegisterEmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
                employee = serializer.save()
                return Response(
                    {"message": "Employee registered successfully", "employee": employee.id},
                    status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(generics.GenericAPIView):
    serializer_class=EmployeeLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class=self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer_class.is_valid(raise_exception=True)
        user=serializer_class.validated_data["user"]
        login(request, user)
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {'id': user.id, 'email': user.email}
        })


class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    @ method_decorator(allowed_users(["Admin"]))
    @ method_decorator(auth_required)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @ method_decorator(allowed_users(["Admin"]))
    @ method_decorator(auth_required)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

    @ method_decorator(allowed_users(["Admin"]))
    @ method_decorator(auth_required)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @ method_decorator(allowed_users(["Admin"]))
    @ method_decorator(auth_required)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    @ method_decorator(allowed_users(["Admin"]))
    @ method_decorator(auth_required)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        with transaction.atomic():
            instance.delete()
            user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
