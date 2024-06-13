from ninja import ModelSchema
from core.models import Vehicle
# from app.serializers.VehicleVariation import VehicleVariationResponseDefault


ModelSchema.model_config['protected_namespaces'] = ()


class VehicleRequestCreate(ModelSchema):

    class Meta:
        model = Vehicle
        exclude = ['id', 'created_at', 'updated_at']


class VehicleResponseDefault(ModelSchema):

    # variations: list[VehicleVariationResponseDefault]

    class Meta:
        model = Vehicle
        fields = '__all__'
