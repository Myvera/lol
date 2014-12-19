__author__ = 'Insung'

from django import template
register = template.Library()

@register.filter

def access(mc, key):
    return mc[key]
