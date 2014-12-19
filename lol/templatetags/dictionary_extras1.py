__author__ = 'Insung'

from django import template
register = template.Library()

@register.filter

def multi(mc, one, sub):
    return mc[one][sub]