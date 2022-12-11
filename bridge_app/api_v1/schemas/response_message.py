from uuid import UUID
from ninja import Schema


class ResponseMessage(Schema):
    message: str


class CreateResponseMessage(ResponseMessage):
    id: UUID
