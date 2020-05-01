#how to create own filters
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')

# register.filter('cut', cut)
#the 1st one is how we want to call it, the 2nd
