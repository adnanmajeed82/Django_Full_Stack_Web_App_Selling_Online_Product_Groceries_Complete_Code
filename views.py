from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Feedback
from .forms import FeedbackForm

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'store/feedback.html', {'form': form})
