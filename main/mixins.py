from main.models import MyTest
from django.core.exceptions import PermissionDenied

# class UserMixin:
#     """
#     permission only user who created task
#     """
#
#     def dispatch(self, request, *args, **kwargs):
#         obj = MyTest.objects.get(pk=kwargs['pk'])
#         if not request.user == obj.user:
#             raise PermissionDenied
#
#         return super(UserMixin, self).dispatch(
#             request, *args, **kwargs
#         )