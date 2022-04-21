from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    SORT_MAP = {'name': 'name',
                'min_price': 'price',
                'max_price': '-price'
                }

    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(SORT_MAP[sort])

    # if sort == 'name':
    #     result = phones.order_by('name')
    # elif sort == 'min_price':
    #     result = phones.order_by('price')
    # elif sort == 'max_price':
    #     result = phones.order_by('-price')
    # else:
    #     result = phones

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # phone = Phone.objects.get(slug=slug)
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
