from django.shortcuts import render
from .models import Product, Orders
from django.db.models import Q
import logging
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View

# Create your views here.

logger = logging.getLogger(__name__)
stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    params = {'products': Product.objects.all()}

    return render(request, 'index.html', params)


def product_view(request, MyID):
    params = {'main_product': Product.objects.get(id=MyID),
              'other_old_products': Product.objects.filter(~Q(id=MyID)).filter(product_arrival_status="old")[:4],
              'other_new_products': Product.objects.filter(~Q(id=MyID)).filter(product_arrival_status="new")[:4]}
    return render(request, 'sproduct.html', params)


def shop(request):
    params = {'products': Product.objects.all()}
    return render(request, 'shop.html', params)


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        thank = True
        id = order.order_id
        param_dict = {

            'MID': 'Your-Merchant-Id-Here',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)

