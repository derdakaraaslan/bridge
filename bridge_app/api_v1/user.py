
from django.forms import ImageField
from ..models import User
from . import api
from ninja import NinjaAPI

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.get("/User/{name}")
def createUser(request, name, surname, password):
    proc = User.objects.create(name=name, surname=surname, password=password)
    proc.save
    return 200, {"name": proc.name, "surname": proc.surname}
