from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    dictionary=dict(dictionary)
    return dictionary.get(str(key))

@register.filter
def get_item_sum_all(dictionary,dictp):
    sum=0
    dictp=dict(dictp)
    for item in dictionary:
        sum+=item.preco*int(dictp[str(item.id)]['quantidade'])
    return sum