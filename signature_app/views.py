from django.shortcuts import render


def generator(request):
    """Render the email signature generator page."""
    return render(request, 'signature_app/generator.html')
