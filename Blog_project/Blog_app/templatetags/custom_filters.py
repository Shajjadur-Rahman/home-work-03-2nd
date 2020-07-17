from django import template

register = template.Library()


def range_filter(value):
    return value[0:300] + "........."


register.filter('range_filter', range_filter)


def range_title_filter(value):
    return value[0:20] + "......."


register.filter('range_title_filter', range_title_filter)
