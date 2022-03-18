from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def replace_page(context, page):

    querydict = context['request'].GET.copy()
    querydict.pop('page', None)
    querydict['page']= page
    return querydict.urlencode()


@register.simple_tag(takes_context=True)
def add_sort(context, sort):

    querydict = context['request'].GET.copy()
    querydict.pop('page', None)

    querydict.pop('sortreverse', None)

    querydict['sort']=sort
    return querydict.urlencode()

@register.simple_tag(takes_context=True)
def add_sortreverse(context, sortreverse):

    querydict = context['request'].GET.copy()
    querydict.pop('page', None)

    querydict.pop('sort', None)

    querydict['sortreverse']=sortreverse
    return querydict.urlencode()
