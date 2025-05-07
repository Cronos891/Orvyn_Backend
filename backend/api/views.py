from rest_framework import viewsets
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
from .serializers import (
    TenantSerializer,
    CompanySerializer,
    CountrySerializer,
    EmployeeSerializer,
    StatesOrProvincesSerializer,
    LocationSerializer,
    CurrencySerializer,
    HealthInsuranceSerializer,
    JobFamilySerializer,
    JobPositionSerializer,
    PayGroupSerializer,
    UnionSerializer,
    UnionSubgroupSerializer,
    BusinessUnitSerializer,
    CostCenterSerializer,
    InternalOrderSerializer,
    WorkScheduledSerializer,
)

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class StatesOrProvincesViewSet(viewsets.ModelViewSet):
    queryset = StatesOrProvinces.objects.all()
    serializer_class = StatesOrProvincesSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currencies.objects.all()
    serializer_class = CurrencySerializer

class HealthInsuranceViewSet(viewsets.ModelViewSet):
    queryset = HealthInsurances.objects.all()
    serializer_class = HealthInsuranceSerializer

class JobFamilyViewSet(viewsets.ModelViewSet):
    queryset = JobFamilies.objects.all()
    serializer_class = JobFamilySerializer

class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPositions.objects.all()
    serializer_class = JobPositionSerializer

class PayGroupViewSet(viewsets.ModelViewSet):
    queryset = PayGroups.objects.all()
    serializer_class = PayGroupSerializer

class UnionViewSet(viewsets.ModelViewSet):
    queryset = Unions.objects.all()
    serializer_class = UnionSerializer

class UnionSubgroupViewSet(viewsets.ModelViewSet):
    queryset = UnionSubgroups.objects.all()
    serializer_class = UnionSubgroupSerializer

class BusinessUnitViewSet(viewsets.ModelViewSet):
    queryset = BusinessUnits.objects.all()
    serializer_class = BusinessUnitSerializer

class CostCenterViewSet(viewsets.ModelViewSet):
    queryset = CostCenters.objects.all()
    serializer_class = CostCenterSerializer

class InternalOrderViewSet(viewsets.ModelViewSet):
    queryset = InternalOrders.objects.all()
    serializer_class = InternalOrderSerializer

class WorkScheduledViewSet(viewsets.ModelViewSet):
    queryset = WorkScheduled.objects.all()
    serializer_class = WorkScheduledSerializer