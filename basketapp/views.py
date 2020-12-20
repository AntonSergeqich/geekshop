from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):
    title = 'корзина'
    basket_item = Basket.objects.filter(user=request.user).order_by('product__category')
    content = {
        'title': title,
        'basket_item': basket_item,
    }
    return render(request, 'basketapp/basket.html', content)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    basket_item = Basket.objects.filter(user=request.user, product=product).first()

    if not basket_item:
        basket_item = Basket(user=request.user, product=product)
    basket_item.price = product.price
    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=pk)

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_item = Basket.objects.filter(user=request.user).order_by('product__category')

        content = {
            'basket_item': basket_item
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', content)

        return JsonResponse({'result': result})
