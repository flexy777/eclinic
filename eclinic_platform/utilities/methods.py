from rest_framework.response import Response
from django.conf import settings




def paginateQueryset(paginator, queryset, serializer_class):
    page = paginator.paginate_queryset(queryset)
    if page is not None:
        serializer = serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(queryset, many=True)
    result = [ x.values()[0] for x in serializer.data ]
    return Response(result)


def toFileUrl(file):
    return settings.SITE_URL+settings.MEDIA_URL + str(file) if(file) else None



def toDateString(date):
    return date.strftime("%d %b %Y %I:%M%p")
