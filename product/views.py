from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import OuterRef, Subquery, Avg
from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse

from product.models import Product, Image, Category, Comment
from product.filteres import ProductFilter


def home(request):
    main_image_subquery = Image.objects.filter(
        product=OuterRef('pk'),
        is_main=True|False
    ).values('image')[:1]

    products = Product.objects.annotate(
        main_image=Subquery(main_image_subquery)
    ).values('pk', 'translations', 'price', 'main_image')

    context = {'products': products}
    return render(request, 'home.html', context)


def get_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    main_image_subquery = Image.objects.filter(
        product=OuterRef('pk'),
    ).values('image')[:1]
    products = Product.objects.filter(category=category).annotate(main_image=Subquery(main_image_subquery)
        ).values('pk', 'translations', 'price', 'main_image')

    products = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = products.page(page)
    except (PageNotAnInteger, EmptyPage):
        products = products.page(1)

    context = {'products': products , 'category': category}
    return render(request , 'product/store.html' , context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        star = request.POST.get('star')
        if request.user.is_authenticated:
            comment = Comment.objects.create(
                product=product,
                owner=request.user,
                text=text,
                star=star or 0
            )
            return redirect(reverse('product:detail' , kwargs={'pk':product.pk}))
        avg_rating = product.comment_set.aggregate(AvgRating=Avg('star'))['star_avg']

        context = {'product': product, 'avg_rating': avg_rating}
        return render(request , 'product/detail.html' , context)



    context = {'product': product}
    return render(request, 'product/detail.html', context)

def store(request):
    main_image_subquery = Image.objects.filter(product=OuterRef('pk')
                                               # is_main=True
    ).values('image')[:1]
    price__gte = request.GET.get('price__gte')
    price__lte = request.GET.get('price__lte')
    if price__gte and price__lte:
        products = Product.objects.filter(price__gte=price__gte , price__lte=price__lte)
    else:
        products = Product.objects.all()


    products = products.annotate(main_image=Subquery(main_image_subquery)
        ).values('pk','translations','price' ,'main_image')

    products = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        products = products.page(page)
    except (PageNotAnInteger, EmptyPage):
        products = products.page(1)

    context = {'products': products }

    return render(request, 'product/store.html', context)




