from rest_framework import serializers
from .models import (
    Tenant,
    Companies,
    Countries,
    Employees,
    StatesOrProvinces,
    Locations,
    Currencies,
    HealthInsurances,
    JobFamilies,
    JobPositions,
    PayGroups,
    Unions,
    UnionSubgroups,
    BusinessUnits,
    CostCenters,
    InternalOrders,
    WorkScheduled,
)

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = Companies
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = Countries
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = Employees
        fields = '__all__'

class StatesOrProvincesSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = StatesOrProvinces
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = Locations
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = Currencies
        fields = '__all__'

class HealthInsuranceSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = HealthInsurances
        fields = '__all__'

class JobFamilySerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = JobFamilies
        fields = '__all__'

class JobPositionSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = JobPositions
        fields = '__all__'

class PayGroupSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = PayGroups
        fields = '__all__'

class UnionSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = Unions
        fields = '__all__'

class UnionSubgroupSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = UnionSubgroups
        fields = '__all__'

class BusinessUnitSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = BusinessUnits
        fields = '__all__'

class CostCenterSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = CostCenters
        fields = '__all__'

class InternalOrderSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = InternalOrders
        fields = '__all__'

class WorkScheduledSerializer(serializers.ModelSerializer):
    tenant_id = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    class Meta:
        model = WorkScheduled
        fields = '__all__'