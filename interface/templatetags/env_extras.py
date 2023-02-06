from os import getenv as env
from django import template

register = template.Library()


@register.simple_tag
def get_env_var():
    return env("url")