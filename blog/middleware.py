from django.shortcuts import redirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class PublicAccessMiddleware(MiddlewareMixin): 
    PUBLIC_URL_NAMES = [
        'index', 
        'login',
        'logout',
        'create_comment',
    ]
    def process_view(self, request, view_func, view_args, view_kwargs):
        current_path = request.path_info
        if current_path.startswith('/admin/'):
            return None
        try:
            current_url_name = request.resolver_match.url_name
        except AttributeError:
            return None
        if current_url_name in self.PUBLIC_URL_NAMES:
            return None
        if request.user.is_authenticated:
            return None 
        return redirect('index')
