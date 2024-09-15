from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def get_error_response(request: HttpRequest, message: str) -> HttpResponse:
    return render(request, 'error.html', {'error': message})
