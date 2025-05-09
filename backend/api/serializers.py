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
    company_location = LocationSerializer(read_only=True)
    company_country = CountrySerializer(read_only=True)
    location_code = serializers.CharField(write_only=True, required=False, allow_null=True)
    country_code = serializers.CharField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Companies
        fields = [
            'tenant_id',
            'company_code',
            'company',
            'company_tax_id',
            'company_address',
            'company_location',
            'company_country',
            'company_status',
            'location_code',
            'country_code'
        ]

    def create(self, validated_data):
        location_code = validated_data.pop('location_code', None)
        country_code = validated_data.pop('country_code', None)

        if location_code:
            try:
                location = Locations.objects.get(location_code=location_code)
                validated_data['company_location'] = location
            except Locations.DoesNotExist:
                raise serializers.ValidationError({'location_code': 'Ubicación no encontrada'})

        if country_code:
            try:
                country = Countries.objects.get(country_code=country_code)
                validated_data['company_country'] = country
            except Countries.DoesNotExist:
                raise serializers.ValidationError({'country_code': 'País no encontrado'})

        return Companies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        location_code = validated_data.pop('location_code', None)
        country_code = validated_data.pop('country_code', None)

        if location_code:
            try:
                location = Locations.objects.get(location_code=location_code)
                instance.company_location = location
            except Locations.DoesNotExist:
                raise serializers.ValidationError({'location_code': 'Ubicación no encontrada'})

        if country_code:
            try:
                country = Countries.objects.get(country_code=country_code)
                instance.company_country = country
            except Countries.DoesNotExist:
                raise serializers.ValidationError({'country_code': 'País no encontrado'})

        instance.company = validated_data.get('company', instance.company)
        instance.company_tax_id = validated_data.get('company_tax_id', instance.company_tax_id)
        instance.company_address = validated_data.get('company_address', instance.company_address)
        instance.company_status = validated_data.get('company_status', instance.company_status)
        instance.save()

        return instance

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