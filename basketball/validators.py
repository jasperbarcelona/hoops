from django.utils.decorators import available_attrs
from functools import wraps
from django.http import JsonResponse,HttpResponse

def form_data(params):
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            missing = []
            data = request.POST
            for param in params:
                if not param in data:
                    missing.append(param)
            if missing:
                return JsonResponse({
                    'status': 'failed',
                    'message': 'Missing argument/s: %s' % missing
                    })
            return func(request, *args, **kwargs)
        return inner
    return decorator