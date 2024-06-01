from django.shortcuts import render


def error_404_view(request, exception):
    context = {"title": "404 | KAloss"}

    return render(request, "404.html", context)
