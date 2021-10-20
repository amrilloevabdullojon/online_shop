from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Min
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here
from django.views.generic import ListView, DetailView

from products.models import ProductModel, BrandModel, CategoryModel, ProductTagModel, SizeModel, ColorModel


class ProductListView(ListView):
    template_name = 'products.html'
    paginate_by = 3

    # queryset = ProductModel.objects.order_by('-pk')
    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')
        color = self.request.GET.get('color')
        size = self.request.GET.get('size')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if brand:
            qs = qs.filter(brand_id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if color:
            qs = qs.filter(color__id=color)

        if size:
            qs = qs.filter(size__id=size)
        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            if sort == '-price':
                qs = qs.order_by('-real_price')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = BrandModel.objects.order_by('-pk')
        context['categories'] = CategoryModel.objects.order_by('-pk')
        context['tags'] = ProductTagModel.objects.order_by('-pk')
        context['sizes'] = SizeModel.objects.order_by('-pk')
        context['color'] = ColorModel.objects.order_by('-pk')

        context['min_price'], context['max_price'] = ProductModel.objects.aggregate(
            Min('real_price'),
            Max('real_price')
        ).values()
        return context


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['related'] = ProductModel.objects.filter(category=self.object.category).exclude(pk=self.object.pk)[:4]
        context['related'] = self.object.category.products.exclude(pk=self.object.pk)[:4]

        return context


class WishListListView(LoginRequiredMixin, ListView):
    template_name = 'favourites.html'
    paginate_by = 4

    def get_queryset(self):
        return self.request.user.wishlist.order_by('-pk')


@login_required
def create_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)

    if request.user in product.wishlist.all():
        product.wishlist.remove(request.user)
    else:
        product.wishlist.add(request.user)

    product.save()

    return redirect(request.GET.get('next', '/'))


def add_to_cart(request, pk):
    cart = request.session.get('cart')
    if not cart:
        cart = []

    if pk not in cart:
        cart.append(pk)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', '/'))