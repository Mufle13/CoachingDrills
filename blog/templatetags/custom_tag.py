from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def replace_page(context, page):

    querydict = context['request'].GET.copy()
    querydict.pop('page', None)
    querydict['page']= page
    return querydict.urlencode()
