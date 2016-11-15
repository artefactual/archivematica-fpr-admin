from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def login(request):
    try:
        user = User.objects.get()
    except User.DoesNotExist:
        messages.error(request, 'User not found!')
    else:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user = auth.login(request, user)
    return redirect(reverse('fpr_index'))
