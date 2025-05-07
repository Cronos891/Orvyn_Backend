from django.contrib import admin
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
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'name', 'created_at')
    search_fields = ('tenant_id', 'name')

@admin.register(Companies)
class CompaniesAdmin(SimpleHistoryAdmin):
    list_display = ('tenant_id', 'company_code', 'company', 'company_status')
    search_fields = ('company_code', 'company', 'company_tax_id')
    list_filter = ('tenant_id', 'company_status')

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'country_code', 'country', 'salary_multiplier')
    search_fields = ('country_code', 'country')
    list_filter = ('tenant_id',)

@admin.register(Employees)
class EmployeesAdmin(SimpleHistoryAdmin):
    list_display = ('tenant_id', 'employee_id', 'full_legal_name', 'payroll_id', 'company_code')
    search_fields = ('employee_id', 'full_legal_name', 'payroll_id', 'national_id', 'tax_id')
    list_filter = ('tenant_id', 'company_code', 'employee_type', 'time_type', 'country')

@admin.register(StatesOrProvinces)
class StatesOrProvincesAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'region_code', 'region', 'country_code')
    search_fields = ('region_code', 'region')
    list_filter = ('tenant_id', 'country_code',)

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'location_code', 'location_name', 'region_code', 'country_code')
    search_fields = ('location_code', 'location_name')
    list_filter = ('tenant_id', 'region_code', 'country_code')

@admin.register(Currencies)
class CurrenciesAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'currency_code', 'currency', 'country_code')
    search_fields = ('currency_code', 'currency')
    list_filter = ('tenant_id', 'country_code',)

@admin.register(HealthInsurances)
class HealthInsurancesAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'health_insurance_code', 'health_insurance_name', 'health_insurance_type')
    search_fields = ('health_insurance_code', 'health_insurance_name')
    list_filter = ('tenant_id', 'health_insurance_type',)

@admin.register(JobFamilies)
class JobFamiliesAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'job_family_name', 'job_family_group', 'job_family_status')
    search_fields = ('job_family_name', 'job_family_group')
    list_filter = ('tenant_id', 'job_family_status',)

@admin.register(JobPositions)
class JobPositionsAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'job_code', 'job_position_name', 'job_family_name')
    search_fields = ('job_code', 'job_position_name', 'job_family_name')
    list_filter = ('tenant_id',)

@admin.register(PayGroups)
class PayGroupsAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'pay_group_code', 'pay_group_name', 'pay_group_frequency', 'company_code')
    search_fields = ('pay_group_code', 'pay_group_name')
    list_filter = ('tenant_id', 'pay_group_frequency', 'company_code')

@admin.register(Unions)
class UnionsAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'union_code', 'union_name')
    search_fields = ('union_code', 'union_name')
    list_filter = ('tenant_id',)

@admin.register(UnionSubgroups)
class UnionSubgroupsAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'subgroup_code', 'union_code', 'subgroup_name', 'category', 'grade_level')
    search_fields = ('subgroup_code', 'subgroup_name')
    list_filter = ('tenant_id', 'union_code', 'category', 'grade_level')

@admin.register(BusinessUnits)
class BusinessUnitsAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'business_unit_id', 'business_unit', 'function', 'sub_function')
    search_fields = ('business_unit_id', 'business_unit', 'function', 'sub_function')
    list_filter = ('tenant_id',)

@admin.register(CostCenters)
class CostCentersAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'cost_center_code', 'cost_center_name', 'company_code', 'status')
    search_fields = ('cost_center_code', 'cost_center_name')
    list_filter = ('tenant_id', 'company_code', 'status')

@admin.register(InternalOrders)
class InternalOrdersAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'internal_order_code', 'internal_order_name', 'company_code', 'status')
    search_fields = ('internal_order_code', 'internal_order_name')
    list_filter = ('tenant_id', 'company_code', 'status')

@admin.register(WorkScheduled)
class WorkScheduledAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'shift_code', 'shift_description', 'company')
    search_fields = ('shift_code', 'shift_description', 'company')
    list_filter = ('tenant_id',)