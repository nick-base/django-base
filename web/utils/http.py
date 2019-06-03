from django.http import HttpResponse
from django.http import JsonResponse

__all__ = [
    'response_success',
    'response_error',
]

SUCCESS_STATUS = 'success'
ERROR_STATUS = 'error'

def response_success(data={}, message=''):
    response = {
        'data': data,
        'status': SUCCESS_STATUS,
        'ResponseCode': '200'
    }
    return JsonResponse(response)

def response_error(data={}, message='', code=500):
    response = {
        'data': data,
        'code': code,
        'message': message,
        'status': ERROR_STATUS,
        'ResponseCode': '200'
    }
    return JsonResponse(response)
