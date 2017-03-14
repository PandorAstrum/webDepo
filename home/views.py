from django.shortcuts import render

from .models import bootstrap_Carousel, owl_PhotoSlide, accordion1_content, accordion2_content, accordion3_content, accordion4_content

# Create your views here.

def homepage(request):
    queryset = bootstrap_Carousel.objects.all()
    Owlquery = owl_PhotoSlide.objects.all()
    accordion1query = accordion1_content.objects.all()
    accordion2img = accordion2_content.objects.values_list('image', flat=True)[0]
    accordion2imgalt = accordion2_content.objects.values_list('name', flat=True)[0]
    accordion2title = accordion2_content.objects.values_list('acc2_title', flat=True)[0]
    accordion2desc = accordion2_content.objects.values_list('acc2_desc', flat=True)[0]
    accordion2link = accordion2_content.objects.values_list('acc2_content_link', flat=True)[0]
    accordion3query = accordion3_content.objects.all()
    accordion4query = accordion4_content.objects.all()
    context = {
        'instance' : queryset,
        'owl' : Owlquery,
        'acc1' : accordion1query,
        'acc2img' : accordion2img,
        'acc2imgalt' : accordion2imgalt,
        'acc2title' : accordion2title,
        'acc2desc' : accordion2desc,
        'acc2link' : accordion2link,
        'acc3' : accordion3query,
        'acc4' : accordion4query,
    }
    return render(request, "index.html", context)

def gamesPage(request):
    return render(request, "index.html", {})

def portfolioPage(request):
    return render(request, "index.html", {})

def blogPage(request):
    return render(request, "index.html", {})

def AboutPage(request):
    return render(request, "index.html", {})