from django.db import models


class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
        # app_label = ''
        # get_latest_by = 'created_at'
        # verbose_name = ''
        # verbose_name_plural = ''


class Vehicle(BaseModel):

    model = models.CharField(max_length=20, null=False, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    origin = models.CharField(max_length=20, null=False, blank=True)
    manufacturer = models.CharField(max_length=20, null=False, blank=True)
    brand = models.CharField(max_length=20, null=False, blank=True)
    factory = models.CharField(max_length=20, null=False, blank=True)
    type = models.CharField(max_length=20, null=False, blank=True)
    model_year = models.IntegerField(null=False)


class VehicleVariation(BaseModel):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='variations')
    name = models.CharField(max_length=20)

    # sizing
    width = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    wheel_base = models.IntegerField(default=0)
    front_track = models.IntegerField(default=0)
    rear_track = models.IntegerField(default=0)
    drag_coefficient = models.FloatField(default=0)
    curb_weight = models.IntegerField(default=0)
    wheel_size = models.IntegerField(default=0)
    front_over = models.IntegerField(default=0)
    rear_over = models.IntegerField(default=0)
    interior_volume = models.IntegerField(default=0)
    front_trunk_volume = models.IntegerField(default=0)
    rear_trunk_volume = models.IntegerField(default=0)

    # power train
    platform = models.CharField(max_length=20)
    drive_type = models.CharField(max_length=20)
    motor_type = models.CharField(max_length=20)
    energy_source = models.CharField(max_length=20)
    energy_volume = models.FloatField(default=0)
    energy_system = models.IntegerField(default=0)

    # 성능
    max_torque = models.IntegerField(default=0)
    max_power = models.IntegerField(default=0)
    max_speed = models.IntegerField(default=0)
    horse_power = models.IntegerField(default=0)


class VehicleUtility(BaseModel):
    variation = models.ForeignKey(VehicleVariation, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    description = models.CharField(max_length=100)


class VehicleEfficiency(BaseModel):
    variation = models.ForeignKey(VehicleVariation, on_delete=models.CASCADE)
    certificated_by = models.CharField(max_length=20)
    combined_range = models.IntegerField(default=0)
    combined_efficiency = models.IntegerField(default=0)
    city_range = models.IntegerField(default=0)
    city_efficiency = models.IntegerField(default=0)
    highway_range = models.IntegerField(default=0)
    highway_efficiency = models.IntegerField(default=0)


class VehicleChargeProfile(BaseModel):
    pass
