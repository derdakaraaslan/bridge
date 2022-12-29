from typing import Any, List
from math import ceil

from ninja import Schema
from ninja.pagination import PaginationBase


class CustomPagination(PaginationBase):
    class Input(Schema):
        page: int
        per_page: int

    class Output(Schema):
        items: List[Any]
        total_item_count: int
        total_page: int
        active_page: int
        per_page: int

    def paginate_queryset(self, queryset, pagination: Input, **params):
        per_page = pagination.per_page if pagination.per_page > 0 and pagination.per_page <= 100 else 10
        total_page = ceil(queryset.count() / per_page)
        page = pagination.page if pagination.page <= total_page and pagination.page > 0 else 1

        return {
            'items': queryset[(page-1)*per_page: page * per_page],
            'total_item_count': queryset.count(),
            'total_page': total_page,
            'active_page': page,
            'per_page': per_page,
        }
