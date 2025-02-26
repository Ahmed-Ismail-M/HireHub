from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from ..models import Employee, User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class RegisterEmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    company = serializers.PrimaryKeyRelatedField(
        queryset=Employee.company.field.related_model.objects.all())
    department = serializers.PrimaryKeyRelatedField(
        queryset=Employee.department.field.related_model.objects.all())
    mobile_number = serializers.CharField(required=True)

    class Meta:
        model = Employee
        fields = [
            'email', 'password', 'first_name', 'last_name', 'company', 'department',
            'status', 'mobile_number', 'address', 'designation', 'hired_on'
        ]

    def validate(self, data):
        """
        Validate that the department belongs to the selected company and email isn't already used
        """
        # Check if email already exists
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})

        # Validate department belongs to company
        company = data.get('company')
        department = data.get('department')
        if company and department:
            if department.company != company:
                raise serializers.ValidationError({
                    "department": "The selected department does not belong to the specified company."
                })

        return data

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')

        user = User.objects.create(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password)
        )
        group, created = Group.objects.get_or_create(name='Employee')
        user.groups.add(group)

        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class EmployeeLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                print(user)
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs


class EmployeeSerializer(serializers.ModelSerializer):
    days_employed = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = [
            'id', 'user', 'full_name', 'company', 'department', 'group', 'status',
            'mobile_number', 'address', 'designation', 'hired_on', 'days_employed', 'email'
        ]
