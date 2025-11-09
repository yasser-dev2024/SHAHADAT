from django.shortcuts import render
from .models import CertificateCategory

def home_view(request):
    # جلب التصنيفات مع جميع القوالب التابعة لها
    categories = CertificateCategory.objects.prefetch_related('templates').all().order_by('name')
    return render(request, 'home.html', {'categories': categories})
