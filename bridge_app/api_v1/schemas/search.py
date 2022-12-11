from typing import List

from ninja import Schema


class SearchSchema(Schema):
    filter: dict = None
    order_by: List[str] = None

    def search_on(self, model, user=None):
        qs = model.objects.filter()
        qs = qs.filter(**self.filter) if self.filter is not None else qs
        qs = qs.order_by(*self.order_by) if self.order_by is not None else qs

        return qs
