from abc import abstractmethod, ABC
from django.db.models import QuerySet


class PermitterBase(ABC):

    @staticmethod
    @abstractmethod
    def create(user, object) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def read(user, object) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def update(user, object) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def delete(user, object) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def search(user, queryset) -> QuerySet:
        pass
