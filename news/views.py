from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView

from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class GenerateRandomUserView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total) # This way we are instructing Celery to execute this function in the background.
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')

class UsersListView(ListView):
    template_name = 'users_list.html'
    model = User