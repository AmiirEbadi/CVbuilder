
from django.shortcuts import redirect

class ProfileCompletionMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_complete:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:profile')