from django import template

register = template.Library()

@register.filter
def getindex(List, i):
    return List[int(i)]

# register.filter('index', index)
