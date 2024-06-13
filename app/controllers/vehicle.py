from ninja import Router
from app.serializers.Vehicle import VehicleResponseDefault, VehicleRequestCreate
from app.serializers.VehicleVariation import VehicleVariationResponseDefault, VehicleVariationRequestCreate
from core.models import Vehicle, VehicleVariation

router = Router()


@router.post('')
def post_vehicle(request, body: VehicleRequestCreate):

    entity = Vehicle()
    entity.model = body.model
    entity.name = body.name
    entity.origin = body.origin
    entity.manufacturer = body.manufacturer
    entity.factory = body.factory
    entity.model_year = body.model_year
    entity.type = body.type
    entity.save()

    return


@router.get('list', response=list[VehicleResponseDefault])
def get_vehicle_list(request):
    entities = Vehicle.objects.all()
    return entities


@router.get('{vehicle_id}', response=VehicleResponseDefault)
def get_vehicle(request, vehicle_id: int):
    entity = Vehicle.objects.get(pk=vehicle_id)

    return entity


@router.post('/variation')
def post_vehicle_variation(request, body: VehicleVariationRequestCreate):

    entity = VehicleVariation()

    print(body)
    for key in body.dict().keys():
        setattr(entity, key, getattr(body, key))

    print(entity)
    entity.save()

    return None


@router.get(
    '{vehicle_id}/variation/list',
    response=list[VehicleVariationResponseDefault],
)
def get_vehicle_variations(request, vehicle_id: int):

    # vehicle = Vehicle.objects.get(id=vehicle_id)

    variations = VehicleVariation.objects.filter(vehicle_id=vehicle_id).all()

    return variations


