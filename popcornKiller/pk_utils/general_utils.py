from django.shortcuts import render


def get_error_response(request, message):
    return render(request, 'error.html', {'error': message})
