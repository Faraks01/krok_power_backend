from rest_framework.permissions import BasePermission


class CreateOrReadOnly(BasePermission):
    """
    The request is a POST, or is a GET request.
    """

    def has_permission(self, request, view):
        return request.method in ('GET', 'HEAD', 'OPTIONS', 'POST')
