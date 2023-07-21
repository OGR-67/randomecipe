from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, token):
    """ Add class attribute, esp. for form inputs and textareas """
    value.field.widget.attrs["class"] = token
    return value
