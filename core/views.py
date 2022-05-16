from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/portafolio/">Portafolio</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def base(request):
    return render(request,"core/base.html")

def about(request):
    return render(request,"core/about.html")

def portafolio(request):
    return render(request,"core/portafolio.html")

def contact(request):
    return render(request,"core/contacto.html")