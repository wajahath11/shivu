from django import template

register = template.Library()

@register.simple_tag
def active_page(request, view_name):
    if not request:
        return ""
    if not request.resolver_match:
        return ""
    if isinstance(view_name, str):
        view_names = view_name.split(',')
    else:
        view_names = [view_name]
    if request.resolver_match.url_name in view_names:
        return "active"
    return ""