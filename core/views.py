from django.shortcuts import render
from certificates.models import CertificateTemplate

def home(request):
    templates = CertificateTemplate.objects.all()
    return render(request, "home.html", {"templates": templates})
