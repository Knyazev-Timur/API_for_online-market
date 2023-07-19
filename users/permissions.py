from rest_framework.permissions import BasePermission


class UserIsActivePermission(BasePermission):
    """ is_activ встроенная проверка, но по требованиям задания она должна быть выполнена,
    вынесена в отдельный класс, чтоб показать понимания, как делаются кастомные проверки"""
    message = "User is not active!"

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False
