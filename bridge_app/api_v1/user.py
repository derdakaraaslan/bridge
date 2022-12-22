from ..models import User
from . import api
from uuid import UUID
from .schemas import UserSchemaIn

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.post("/users", tags=["User"], response={200: UUID, 400: str, 403: str})
def create(request, payload: UserSchemaIn):
    if User.objects.filter(email=payload.dict()["email"]).exists():
        return 400, {"message": "Mail adresi zaten kayıtlı"}

    data = payload.dict()
    object = User(**data)
    object.set_password(payload.password)
    object.save()

    return 200, {"message": "Kullanıcı başarıyla oluşturuldu", "id": object.id}
