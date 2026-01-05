from .models import APILog

class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Log only API requests
        if request.path.startswith('/api/'):
            user = request.user if request.user.is_authenticated else None
            ip = self.get_client_ip(request)
            
            try:
                APILog.objects.create(
                    user=user,
                    endpoint=request.path,
                    method=request.method,
                    status_code=response.status_code,
                    ip_address=ip
                )
            except Exception:
                pass # Fail silently to avoiding blocking response

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
