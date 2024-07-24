from django import template

register = template.Library()

@register.filter
def star_range(number):
    return range(int(number))

