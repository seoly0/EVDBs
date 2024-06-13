from core.models import VehicleVariation
from ninja import ModelSchema


class VehicleVariationRequestCreate(ModelSchema):

    vehicle_id: int

    class Meta:
        model = VehicleVariation
        exclude = ('id', 'updated_at', 'created_at')


class VehicleVariationResponseDefault(ModelSchema):

    vehicle_id: int

    class Meta:
        model = VehicleVariation
        exclude = ('vehicle', )

