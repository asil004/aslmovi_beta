import json

from django import template
import requests

register = template.Library()


# @register.simple_tag()
@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter("get_response")
@register.simple_tag()
def get_response(url):
    r = requests.get(url)
    r.raise_for_status()
    data = json.loads(r.text)
    # new_data = []
    # new_dict = {}
    # for i in data:
    #     for indx,val in i.items():

    return data


@register.filter("is_txt")
@register.simple_tag()
def is_txt(data):
    if data.endswith('txt'):
        return True
    return False
