from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QvQgnQw8FoE5zeXxlN5T6GzZ4RSa8MKl1mPa3kcZnKhaBopPxVnmjY5GK5Ui0x0KBiuSGlPuGaiNAlt2QrKyqDu00MiaGTNej',
        'client_secret': 'sk_test_51QvQgnQw8FoE5zeXofCiiCbtPYlTCX4eRy8fnUXWSqrjz6cL7Gg5J7IGGT92RUp3IMRFLik4NzCeokUOkrZ8fNC100b74FOLEs',
    }

    return render(request, template, context)