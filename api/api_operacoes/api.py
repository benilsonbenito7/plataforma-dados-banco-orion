from ninja_extra import NinjaExtraAPI
from .controladores.controladores import router

api = NinjaExtraAPI(
    title="Banco Orion API",
    version="1.0.0"
)
api.add_router('v1/', router)