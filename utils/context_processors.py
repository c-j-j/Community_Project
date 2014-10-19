import settings


def community(request):
    return {
        'site_name': settings.SITE_NAME,
        'request': request
    }