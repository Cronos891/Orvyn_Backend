from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tenants', views.TenantViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'states-or-provinces', views.StatesOrProvincesViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'currencies', views.CurrencyViewSet)
router.register(r'health-insurances', views.HealthInsuranceViewSet)
router.register(r'job-families', views.JobFamilyViewSet)
router.register(r'job-positions', views.JobPositionViewSet)
router.register(r'pay-groups', views.PayGroupViewSet)
router.register(r'unions', views.UnionViewSet)
router.register(r'union-subgroups', views.UnionSubgroupViewSet)
router.register(r'business-units', views.BusinessUnitViewSet)
router.register(r'cost-centers', views.CostCenterViewSet)
router.register(r'internal-orders', views.InternalOrderViewSet)
router.register(r'work-scheduled', views.WorkScheduledViewSet)

urlpatterns = [
    path('', include(router.urls)),
]