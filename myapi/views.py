from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.views import generic

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import CustomUserForm, UpdateCustomUserForm, JobForm, UpdateJob, LoginForm, RegistrationForm
from .models import CustomUser, Job, Machine, Timecard
from django.views.generic import(
    DeleteView,
    ListView,
    UpdateView
)

@user_passes_test(lambda u:u.is_admin, login_url=reverse_lazy('home'))
def create_user(request):
    form = CustomUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:All_Users'))
    context = {
        'form': form
    }
    return render(request,"UserTemps/create_user.html",context)

def user_registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request,"registration/register.html",context)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'UserTemps/update_user.html'
    fields = [
        'name'
    ]
    success_url = reverse_lazy('users:All_Users')

class UsersListView(PermissionRequiredMixin,ListView):
    permission_required = 'is_admin'
    redirect_field_name = '/'
    model = CustomUser
    paginate_by = 100
    context_object_name = 'users_list'
    queryset = CustomUser.objects.all()
    template_name = 'UserTemps/users_list_view.html'

class delete_user(DeleteView):
    template_name = 'UserTemps/delete_user.html'
    model = CustomUser
    success_url = reverse_lazy('users:All_Users')

def get_jobs(request):
    jobs = CustomUser.objects.filter()
# Create your views here.
