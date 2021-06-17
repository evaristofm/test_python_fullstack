import requests
from django.shortcuts import render
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



def produtos(request):
    r = requests.get('https://no2gru7ua3.execute-api.us-east-1.amazonaws.com/')
    produtos = r.json()
    context = {'produtos': produtos}

    for produto in produtos['produtos']:
       context.update(produto)    
    return render(request, "produto/produto_list2.html", context)


# View responśavel pelo login e redirecionar para pág principal

class CustomLoginView(LoginView):
    template_name = 'produto/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('product:all-products')

# View responśavel pelo cadastro de novos usuários
class RegisterPage(FormView):
    template_name = 'produto/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('product:all-products')

    # Sobrescrevendo o método para verificar e logar o usuário 
    # e salvar o formulário de registro
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)



class ProductListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = 'products'
    paginate_by = 5

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r = requests.get('https://no2gru7ua3.execute-api.us-east-1.amazonaws.com/')
        produtos = r.json()
        
        context['produtos'] = produtos
        return context  
    

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
    



