
import logging
from pydoc import locate

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import JsonResponse

from .api_v1.schemas import ResponseMessage

logger = logging.getLogger(__name__)


class UnauthorizedException(Exception):
    """Throwed when the user is unauthorized for the requested operation."""
    pass



def unauthorized_handler(request, e: UnauthorizedException):
    return JsonResponse(ResponseMessage(message="Yapmaya çalıştığınız işlem için yetkiniz yok.").dict(), status=403)



def validation_error_handler(request, e: ValidationError):
    return JsonResponse(ResponseMessage(message=e.message).dict(), status=400)


def generic_handler(request, e: Exception):
    logger.exception(e)
    message = "Bilinmeyen bir hata oluştu." if not settings.DEBUG else str(e)
    return JsonResponse(ResponseMessage(message=message).dict(), status=400)
