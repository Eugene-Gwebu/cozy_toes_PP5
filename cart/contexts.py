from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = Decimal(settings.STANDARD_DELIVERY_FEE)
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, id=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product': product,
            'quantity': quantity,
        })

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context