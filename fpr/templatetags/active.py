from django.template import Library
import math

register = Library()

@register.simple_tag
def active(request, pattern):
    if request.path.startswith(pattern) and pattern != '/':
        return 'active'
    elif request.path == pattern == '/':
        return 'active'
    else:
        return ''