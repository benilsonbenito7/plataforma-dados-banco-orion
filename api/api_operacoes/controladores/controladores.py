from ninja import Router
from ..services.clientes_services import ClienteService
from ..shemas.shemas import ClienteSchemaOut, ClienteSchemaIn

router = Router()

@router.post("/clientes", response=ClienteSchemaOut)
def criar_cliente(request, data: ClienteSchemaIn):
    return ClienteService.criar_cliente(data)