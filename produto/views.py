from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import ( 
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Produto


class CustomLoginView(LoginView):
    template_name = 'produto/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('product:all-products')

class RegisterPage(FormView):
    template_name = 'produto/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('product:all-products')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class ProductListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = 'products'
    paginate_by = 5

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Produto
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('product:all-products')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    context_object_name = 'product'
    success_url = reverse_lazy('product:all-products')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = '__all__'
    context_object_name = 'product'
    success_url = reverse_lazy('product:all-products')

 


