from django.db import models
from simple_history.models import HistoricalRecords


class Tenant(models.Model):
    tenant_id = models.CharField(primary_key=True, max_length=50, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tenant_id


class Companies(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    company_code = models.CharField(primary_key=True, max_length=50)
    company = models.CharField(max_length=255, blank=True, null=True)
    company_tax_id = models.CharField(max_length=100, blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_location = models.ForeignKey('Locations', on_delete=models.CASCADE, blank=True, null=True, db_column='company_location')
    company_country = models.ForeignKey('Countries', on_delete=models.CASCADE, blank=True, null=True, db_column='company_country')
    company_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    class Meta:
        managed = True
        db_table = 'companies'


class Countries(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    country_code = models.CharField(primary_key=True, max_length=50)
    country = models.CharField(max_length=100, blank=True, null=True)
    salary_multiplier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'countries'


class Employees(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    employee_id = models.CharField(primary_key=True, max_length=50)
    payroll_id = models.CharField(max_length=50, blank=True, null=True)
    full_legal_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    original_hire_date = models.DateField(blank=True, null=True)
    continuous_service_date = models.DateField(blank=True, null=True)
    company_service_date = models.DateField(blank=True, null=True)
    years_of_service = models.IntegerField(blank=True, null=True)
    scheduled_weekly_hours = models.ForeignKey('WorkScheduled', on_delete=models.SET_NULL, blank=True, null=True, db_column='scheduled_weekly_hours')
    employee_type = models.CharField(max_length=50, blank=True, null=True)
    time_type = models.CharField(max_length=50, blank=True, null=True)
    job_code = models.ForeignKey('JobPositions', on_delete=models.SET_NULL, blank=True, null=True, db_column='job_code', related_name='employees_by_job_code')
    job_position_name = models.ForeignKey('JobPositions', on_delete=models.SET_NULL, blank=True, null=True, db_column='job_position_name', related_name='employees_by_job_position_name')
    job_profile = models.ForeignKey('JobPositions', on_delete=models.SET_NULL, blank=True, null=True, db_column='job_profile', related_name='employees_by_job_profile')
    job_family_name = models.ForeignKey('JobPositions', on_delete=models.SET_NULL, blank=True, null=True, db_column='job_family_name', related_name='employees_by_job_family_name')
    job_family_group = models.ForeignKey('JobPositions', on_delete=models.SET_NULL, blank=True, null=True, db_column='job_family_group', related_name='employees_by_job_family_group')
    business_unit = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='business_unit', related_name='employees_by_business_unit')
    function = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='function', related_name='employees_by_function')
    sub_function = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='sub_function', related_name='employees_by_sub_function')
    country = models.ForeignKey('Countries', on_delete=models.SET_NULL, blank=True, null=True, db_column='country')
    region = models.ForeignKey('StatesOrProvinces', on_delete=models.SET_NULL, blank=True, null=True, db_column='region_code')
    location_code = models.ForeignKey('Locations', on_delete=models.SET_NULL, blank=True, null=True, db_column='location_code', related_name='employees_by_location_code')
    location_name = models.ForeignKey('Locations', on_delete=models.SET_NULL, blank=True, null=True, db_column='location_name', related_name='employees_by_location_name')
    address_street = models.CharField(max_length=255, blank=True, null=True)
    address_number = models.CharField(max_length=20, blank=True, null=True)
    address_floor = models.CharField(max_length=10, blank=True, null=True)
    work_arrangement = models.CharField(max_length=50, blank=True, null=True)
    onsite_work_from_home_pct = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    company_code = models.ForeignKey('Companies', on_delete=models.SET_NULL, blank=True, null=True, db_column='company_code', related_name='employees_by_company_code')
    cost_center_code = models.ForeignKey('CostCenters', on_delete=models.SET_NULL, blank=True, null=True, db_column='cost_center_code', related_name='employees_by_cost_center_code')
    cost_center_name = models.ForeignKey('CostCenters', on_delete=models.SET_NULL, blank=True, null=True, db_column='cost_center_name', related_name='employees_by_cost_center_name')
    internal_order_code = models.ForeignKey('InternalOrders', on_delete=models.SET_NULL, blank=True, null=True, db_column='internal_order_code', related_name='employees_by_internal_order_code')
    internal_order_name = models.ForeignKey('InternalOrders', on_delete=models.SET_NULL, blank=True, null=True, db_column='internal_order_name', related_name='employees_by_internal_order_name')
    union_name = models.ForeignKey('UnionSubgroups', on_delete=models.SET_NULL, blank=True, null=True, db_column='union_name', related_name='employees_by_union_name')
    manager_id = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='manager_id', related_name='managed_employees')
    manager_full_legal_name = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='manager_full_legal_name', related_name='employees_managed_by_full_name')
    manager_first_name = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='manager_first_name', related_name='employees_managed_by_first_name')
    manager_last_name = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='manager_last_name', related_name='employees_managed_by_last_name')
    management_level_1 = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='management_level_1', related_name='employees_at_management_level_1')
    management_level_2 = models.ForeignKey('BusinessUnits', on_delete=models.SET_NULL, blank=True, null=True, db_column='management_level_2', related_name='employees_at_management_level_2')
    pay_group_name = models.ForeignKey('PayGroups', on_delete=models.SET_NULL, blank=True, null=True, db_column='pay_group_name', related_name='employees_by_pay_group_name')
    pay_rule = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey('UnionSubgroups', on_delete=models.SET_NULL, blank=True, null=True, db_column='category', related_name='employees_by_category')
    grade_level = models.ForeignKey('UnionSubgroups', on_delete=models.SET_NULL, blank=True, null=True, db_column='grade_level', related_name='employees_by_grade_level')
    base_monthly_salary = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey('Currencies', on_delete=models.SET_NULL, blank=True, null=True, db_column='currency_code')
    gender = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ]
        )
    race_ethnicity = models.CharField(max_length=100, blank=True, null=True)
    disability = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    corporate_email = models.CharField(max_length=100, blank=True, null=True)
    personnel_email = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_code = models.CharField(max_length=20, blank=True, null=True)
    bank_account_number = models.CharField(max_length=30, blank=True, null=True)
    bank_account_type = models.CharField(max_length=30, blank=True, null=True)
    bank_cbu = models.CharField(max_length=30, blank=True, null=True)
    health_insurance_code = models.ForeignKey('HealthInsurances', on_delete=models.SET_NULL, blank=True, null=True, db_column='health_insurance_code', related_name='employees_by_health_insurance_code')
    health_insurance_name = models.ForeignKey('HealthInsurances', on_delete=models.SET_NULL, blank=True, null=True, db_column='health_insurance_name', related_name='employees_by_health_insurance_name')
    health_insurance_plan = models.ForeignKey('HealthInsurances', on_delete=models.SET_NULL, blank=True, null=True, db_column='health_insurance_plan', related_name='employees_by_health_insurance_plan')
    health_insurance_credential_number = models.CharField(max_length=100, blank=True, null=True)
    apply_withholding_cap = models.CharField(max_length=10, blank=True, null=True)
    apply_proration = models.CharField(max_length=10, blank=True, null=True)
    status_of_employee = models.CharField(max_length=50, blank=True, null=True)

    # Add historical records tracking
    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'employees'


class StatesOrProvinces(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    region_code = models.CharField(primary_key=True, max_length=10)
    region = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='country_code', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'states_or_provinces'


class Locations(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    location_code = models.CharField(primary_key=True, max_length=50)
    location_name = models.CharField(max_length=100, blank=True, null=True)
    region_code = models.ForeignKey(StatesOrProvinces, on_delete=models.CASCADE, db_column='region_code', blank=True, null=True)
    country_code = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='country_code', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'locations'


class Currencies(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    currency_code = models.CharField(primary_key=True, max_length=10)
    currency = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='country_code', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'currencies'


class HealthInsurances(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    health_insurance_code = models.CharField(primary_key=True, max_length=50)
    health_insurance_name = models.CharField(max_length=100, blank=True, null=True)
    health_insurance_plan = models.CharField(max_length=100, blank=True, null=True)
    health_insurance_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'health_insurances'


class JobFamilies(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    job_family_name = models.CharField(primary_key=True, max_length=100)
    job_family_group = models.CharField(max_length=100, blank=True, null=True)
    job_family_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'job_families'


class JobPositions(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    job_code = models.CharField(primary_key=True, max_length=50)
    job_position_name = models.CharField(max_length=100, blank=True, null=True)
    job_profile = models.CharField(max_length=100, blank=True, null=True)
    job_family_name = models.ForeignKey(JobFamilies, on_delete=models.CASCADE, db_column='job_family_name', blank=True, null=True)
    job_family_group = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'job_positions'


class PayGroups(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    pay_group_code = models.CharField(primary_key=True, max_length=50)
    pay_group_name = models.CharField(max_length=100, blank=True, null=True)
    pay_group_frequency = models.CharField(max_length=50, blank=True, null=True)
    company_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pay_groups'


class Unions(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    union_code = models.CharField(primary_key=True, max_length=50)
    union_name = models.CharField(max_length=100, blank=True, null=True)
    employee_contributions = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    employee_contributions_non_members = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    employer_contribution = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'unions'


class UnionSubgroups(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    subgroup_code = models.CharField(primary_key=True, max_length=50)
    union_code = models.ForeignKey(Unions, on_delete=models.CASCADE, db_column='union_code', blank=True, null=True)
    subgroup_name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    grade_level = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'union_subgroups'

class BusinessUnits(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    business_unit_id = models.CharField(primary_key=True, max_length=50)
    business_unit = models.CharField(max_length=100, blank=True, null=True)
    function = models.CharField(max_length=100, blank=True, null=True)
    sub_function = models.CharField(max_length=100, blank=True, null=True)
    manager_id = models.CharField(max_length=50, blank=True, null=True)
    manager_full_legal_name = models.CharField(max_length=255, blank=True, null=True)
    manager_first_name = models.CharField(max_length=100, blank=True, null=True)
    manager_last_name = models.CharField(max_length=100, blank=True, null=True)
    management_level_1 = models.CharField(max_length=100, blank=True, null=True)
    management_level_2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'business_units'


class CostCenters(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    cost_center_code = models.CharField(primary_key=True, max_length=50)
    cost_center_name = models.CharField(max_length=100, blank=True, null=True)
    company_code = models.CharField(max_length=50, blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cost_centers'


class InternalOrders(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    internal_order_code = models.CharField(primary_key=True, max_length=50)
    internal_order_name = models.CharField(max_length=100, blank=True, null=True)
    company_code = models.CharField(max_length=50, blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'internal_orders'


class WorkScheduled(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    shift_code = models.CharField(primary_key=True, max_length=50)
    shift_description = models.CharField(max_length=255, blank=True, null=True)
    shift_working_hours = models.CharField(max_length=100, blank=True, null=True)
    scheduled_weekly_hours = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'work_scheduled'