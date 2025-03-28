from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models.Rental import Rental
from app.models.Ship import Ship

def app(request):
    model_query = request.GET.get('model', '').strip()
    size_query = request.GET.get('size', '')
    category_query = request.GET.get('category', '')
    crew_query = request.GET.get('crew', '')
    sort_by = request.GET.get('sort', 'price-asc')

    queryset = Ship.objects.all()

    if model_query:
        queryset = queryset.filter(name__icontains=model_query.lower())
    if size_query:
        queryset = queryset.filter(size__name=size_query)
    if category_query:
        queryset = queryset.filter(category__name=category_query)
    if crew_query:
        try:
            crew_val = int(crew_query)
            if crew_val == 3:
                queryset = queryset.filter(crew__gte=3)
            else:
                queryset = queryset.filter(crew=crew_val)
        except ValueError:
            pass

    reverse_sort = sort_by.endswith('-desc')
    sort_key = sort_by.replace('-asc', '').replace('-desc', '')

    if sort_key == 'price':
        order_by_field = '-price' if reverse_sort else 'price'
    elif sort_key == 'name':
        order_by_field = '-name' if reverse_sort else 'name'
    else:
        order_by_field = 'price'

    queryset = queryset.order_by(order_by_field)

    filtered_ships = queryset

    paginator = Paginator(filtered_ships, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)


    context = {
        'page_obj': page_obj,
        'current_filters': {
            'model': model_query,
            'size': size_query,
            'category': category_query,
            'crew': crew_query,
        },
        'current_sort': sort_by,
        'query_params': request.GET.urlencode(),
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tos(request):
    return render(request, 'tos.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def faq(request):
    return render(request, 'faq.html')

def ship_detail_view(request, ship_id):
    ship = get_object_or_404(Ship, id=ship_id)
    context = {'ship': ship, 'is_authenticated': request.user.is_authenticated}
    return render(request, 'ship_detail.html', context)

def get_profile(request):
    return render(request, 'profile.html', {
        'user': request.user,
        'rentals': Rental.objects.filter(user=request.user)
    })

def add_to_rental(request, ship_id):
    ship = get_object_or_404(Ship, id=ship_id)
    duration = int(request.POST.get('duration', '1'))
    if not request.user.is_authenticated:
        return redirect('login')

    Rental.objects.create(
        user=request.user,
        ship=ship,
        duration=duration
    )

    return redirect('profile')