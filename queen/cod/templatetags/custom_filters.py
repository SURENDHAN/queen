from django import template

register = template.Library()

@register.filter
def add(value, arg):
    """
    Custom template filter to add two values.
    :param value: The first value.
    :param arg: The value to add to the first value.
    :return: The sum of value and arg.
    """
    return value + arg
