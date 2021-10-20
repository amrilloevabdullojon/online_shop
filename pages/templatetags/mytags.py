from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def get_url_lang(request, lang):
    url = request.path.split('/')
    url[1] = lang
    url = '/'.join(url)
    return url


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


@register.simple_tag
def get_heart_icon(request, product):
    if request.user in product.wishlist.all():
        return static('/img/icon/iconmonstr-favorite-5-16-1.png')
    return static('/img/icon/heart.png')


@register.simple_tag
def get_cart_count(request):
    cart = request.session.get('cart')
    if cart:
        return len(cart)
    return 0


@register.filter
def in_cart(product, request):
    return product in request.session.get('cart', [])

# @register.simple_tag
# def get_heart_icon(request, product):
#     icon = '/img/icon/heart.png'
#     if request.user in product.wishlist.all():
#         icon = '/img/icon/iconmonstr-favorite-5-24.png'
#     return static(icon)
