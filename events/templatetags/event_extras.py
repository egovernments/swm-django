from django import template

register = template.Library()

def cute(value):
    """Removes all values of arg from the given string"""
    return value.replace('images', 'cropped')

register.filter('cute', cute)
