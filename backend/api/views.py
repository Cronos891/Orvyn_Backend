from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Companies.objects.all()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(company_code__icontains=search) |
                Q(company__icontains=search) |
                Q(company_tax_id__icontains=search) |
                Q(company_address__icontains=search) |
                Q(company_location__location_name__icontains=search) |
                Q(company_country__country__icontains=search)
            )
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'message': 'Compañía creada exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error al crear la compañía',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                'message': 'Compañía actualizada exitosamente',
                'data': serializer.data
            })
        return Response({
            'message': 'Error al actualizar la compañía',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class StatesOrProvincesViewSet(viewsets.ModelViewSet):
    queryset = StatesOrProvinces.objects.all()
    serializer_class = StatesOrProvincesSerializer

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

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