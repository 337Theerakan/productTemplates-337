from django.shortcuts import render

def electronics(request):
    products_dict = {
        'product1': 'Mac',
        'product2': 'iPhone',
        'product3': 'Laptop'
    }
    return render(request, 'productApp/products.html', products_dict)

def toys(request):
    products_dict = {
        'product1': 'Figure',
        'product2': 'Drone',
        'product3': 'Remote car'
    }
    return render(request, 'productApp/products.html', products_dict)

def shoes(request):
    products_dict = {
        'product1': 'Nike',
        'product2': 'Adidas',
        'product3': 'Reebok'
    }
    return render(request, 'productApp/products.html', products_dict)

def index(request): 
    return render(request, 'productApp/index.html')  # Corrected here
