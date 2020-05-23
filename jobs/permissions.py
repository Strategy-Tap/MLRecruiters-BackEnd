from typing import Any

from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: Any, obj: Any) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.customer == request.user
