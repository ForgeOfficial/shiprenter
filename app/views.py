from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

ships_list = [
    { 'id': 1, 'name': "C2 Hercules", 'category': "Transport", 'size': "Large", 'crew': 2, 'price': 400, 'description': "Heavy military transport vessel", 'image': "https://robertsspaceindustries.com/i/387f877bf5aae2c4dc6e32568d621473b5d4d79e/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjReskpcDUyTPuKfT2cePUz4jof5hYcpd6LjZx)/source.jpg" },
    { 'id': 2, 'name': "Avenger Titan", 'category': "Combat", 'size': "Petit", 'crew': 1, 'price': 60, 'description': "Versatile fighter with cargo space", 'image': "https://robertsspaceindustries.com/i/8bb4b3fd088d291cbb41fe93451813286579eb47/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResj7DeDFVgu6nYBNEj98TDN2Cw78Ke4wLqU)/source.jpg"},
    { 'id': 3, 'name': "Freelancer MAX", 'category': "Transport", 'size': "Moyen", 'crew': 2, 'price': 150, 'description': "Medium-haul cargo transport", 'image': "https://robertsspaceindustries.com/i/c4f88e02fad2d60c1da178f3f2c8ccbb79152704/resize(910,512,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResjdmBNkPP8gi6Sig2xG6q9wtXFT1AkNQ7x)/source.jpg"},
    { 'id': 4, 'name': "600i Explorer", 'category': "Exploration", 'size': "Large", 'crew': 3, 'price': 475, 'description': "Luxury exploration vessel", 'image': "https://robertsspaceindustries.com/i/bbfd42b3a1a3c30b170da468a56e2ffaec6980e9/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResjqeFfVoF43f38XfD8N5eYmrHRC4QsX4aJ)/source.jpg"},
    { 'id': 5, 'name': "Aurora MR", 'category': "Transport", 'size': "Petit", 'crew': 1, 'price': 30, 'description': "Ideal starter ship for beginners", 'image': "https://robertsspaceindustries.com/i/68c3d71abaf408f2f3b0da1daae05951d5e9286d/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjReseYxot7rosRLQ8WUzNCSJT36TaEZiv51Fk)/source.jpg"},
    { 'id': 6, 'name': "Hammerhead", 'category': "Combat", 'size': "Large", 'crew': 3, 'price': 725, 'description': "Heavily armed combat corvette", 'image': "https://robertsspaceindustries.com/i/40c4b873cfded1a43cb1a156e6bfb31c7ee50e6c/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResez5qZ3dGzZTJPSnuHTV1Ri72MM8BN93xS)/source.jpg"},
    { 'id': 7, 'name': "Mercury Star Runner", 'category': "Transport", 'size': "Moyen", 'crew': 2, 'price': 260, 'description': "Fast ship for data/cargo running", 'image': "https://robertsspaceindustries.com/i/968944e4818ed482e8ca891152eec706ce5575ce/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjReseM2Qd3hg33nVNrZr93SXcfBLpXPPoyseW)/source.jpg"},
    { 'id': 8, 'name': "Constellation Aquila", 'category': "Exploration", 'size': "Large", 'crew': 2, 'price': 315, 'description': "Exploration vessel with rover", 'image': "https://robertsspaceindustries.com/i/96ab2cd07712ae3b381612a2dc8cff27a03ab474/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResip8x1HFMuqNdAyYTfKv58fCqza2364ENA)/source.jpg"},
    { 'id': 9, 'name': "Prospector", 'category': "Exploration", 'size': "Petit", 'crew': 1, 'price': 155, 'description': "Specialized mining vessel", 'image': "https://robertsspaceindustries.com/i/e0ef3c4f03e54d27e0aa7d6bfbd10826f1d9316b/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResjdghv76XEu5GJ6s2qHYtkrcApa8AuqkWi)/source.jpg"},
    { 'id': 10, 'name': "Carrack", 'category': "Exploration", 'size': "Large", 'crew': 3, 'price': 600, 'description': "Long-duration exploration vessel", 'image': "https://robertsspaceindustries.com/i/5a176dc57589f18effd841146ef5a37e88892aee/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResijpd9a1QppWGLqGr3g6nG4GJrw2mPpW4n)/source.jpg"},
    { 'id': 11, 'name': "Cutlass Black", 'category': "Combat", 'size': "Moyen", 'crew': 2, 'price': 110, 'description': "Versatile combat and transport ship", 'image': "https://robertsspaceindustries.com/i/b448409d06251a5d7c4a7c48c2933f0106a0b1ff/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjReseBZjgJWUXGK7SDMJB61YTBmpnZYUiSvSr)/source.jpg"},
    { 'id': 12, 'name': "Vulture", 'category': "Combat", 'size': "Petit", 'crew': 1, 'price': 175, 'description': "Light fighter with salvage capabilities", 'image': "https://robertsspaceindustries.com/i/1af4ed74b973d5b0b5a9a52670c7c2eddd26cb93/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjReskTMVfUvCXkUHEzpj36eNYEXuqMrHr275p)/source.jpg"},
    { 'id': 13, 'name': "Starfarer", 'category': "Transport", 'size': "Large", 'crew': 3, 'price': 300, 'description': "Refueling ship for long journeys", 'image': "https://robertsspaceindustries.com/i/007c2d99fe6fe4f247dc8a067670345f6f49059a/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjReseeJ8UTcvBY2rAEMjJqVuJLZXtYkyXM918)/source.jpg"},
    { 'id': 14, 'name': "Cutlass Red", 'category': "Combat", 'size': "Moyen", 'crew': 2, 'price': 135, 'description': "Medical variant of the Cutlass", 'image': "https://robertsspaceindustries.com/i/fac734628c93a3bc5163570403de8d6008b22439/resize(1820,1024,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjReskfBtT1vzYFaw6fbz4Ly8762W5tPFVNwTc)/source.jpg"},
    { 'id': 15, 'name': "Defender", 'category': "Combat", 'size': "Moyen", 'crew': 2, 'price': 220, 'description': "Banu fighter with unique design", 'image': "https://robertsspaceindustries.com/i/f0591cce6c52b83921eda1a63a957eaeb3018396/resize(910,512,cover,ADdPNihJzmPbNuTnFsH1DqUeqBRpXdSXVVtgJTyDDgscGKrzJuoFjResjqYDYeRY8q9ugefhioggnXHfpwouJVn3p)/source.jpg"},
]

def app(request):
    model_query = request.GET.get('model', '').strip()
    size_query = request.GET.get('size', '')
    category_query = request.GET.get('category', '')
    crew_query = request.GET.get('crew', '')
    sort_by = request.GET.get('sort', 'price-asc')

    filtered_ships = list(ships_list)

    if model_query:
        filtered_ships = [s for s in filtered_ships if model_query.lower() in s.get('name', '').lower()]
    if size_query:
        filtered_ships = [s for s in filtered_ships if s.get('size') == size_query]
    if category_query:
        filtered_ships = [s for s in filtered_ships if s.get('category') == category_query]
    if crew_query:
        try:
            crew_val = int(crew_query)
            if crew_val == 3:
                filtered_ships = [s for s in filtered_ships if s.get('crew', 0) >= 3]
            else:
                filtered_ships = [s for s in filtered_ships if s.get('crew') == crew_val]
        except ValueError:
            pass

    reverse_sort = sort_by.endswith('-desc')
    sort_key = sort_by.replace('-asc', '').replace('-desc', '')

    if sort_key == 'price':
        filtered_ships.sort(key=lambda s: s.get('price', 0), reverse=reverse_sort)
    elif sort_key == 'name':
        filtered_ships.sort(key=lambda s: s.get('name', ''), reverse=reverse_sort)
    else:
        filtered_ships.sort(key=lambda s: s.get('price', 0), reverse=False)

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
    ship = next((s for s in ships_list if s['id'] == ship_id), None)
    context = {'ship': ship}
    return render(request, 'ship_detail.html', context)

def cart(request):
    return render(request, 'cart.html')

def add_to_cart(request, ship_id):
    ship = next((s for s in ships_list if s['id'] == ship_id), None)
    if ship:
        cart = request.session.get('cart', [])
        cart.append(ship)
        request.session['cart'] = cart
        messages.success(request, f"{ship['name']} has been added to your cart.")
    else:
        messages.error(request, "Ship not found.")
    return redirect('app')