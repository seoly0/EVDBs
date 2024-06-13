from ninja import NinjaAPI
from .vehicle import router as vehicle_router

api = NinjaAPI()

api.add_router('vehicle', vehicle_router)
