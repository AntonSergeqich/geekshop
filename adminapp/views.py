from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View

from adminapp.forms import ShopUserAdminEditForm, ProductCreate, ProductEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#    title = 'admin/users'
#
#    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#    content = {
#        'title': title,
#        'objects': users_list,
#    }
#
#    return render(request, 'adminapp/users.html', content)


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#@user_passes_test(lambda u: u.is_superuser)
#def user_create(request):
#    title = 'admin/user_create'
#
#    if request.method == 'POST':
#        user_form = ShopUserRegisterForm(request.POST, request.FILES)
#        if user_form.is_valid():
#            user_form.save()
#            return HttpResponseRedirect(reverse('admin:users'))
#    else:
#        user_form = ShopUserRegisterForm()
#
#    content = {
#        'title': title,
#        'update_form': user_form,
#    }
#
#    return render(request, 'adminapp/user_update.html', content)

class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация пользователя"
        return context


#@user_passes_test(lambda u: u.is_superuser)
#def user_update(request, pk):
#    title = 'admin/user_update'
#
#    edit_user = get_object_or_404(ShopUser, pk=pk)
#    if request.method == "POST":
#        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#        if edit_form.is_valid():
#            edit_form.save()
#            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
#    else:
#
#        edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#    content = {
#        'title': title,
#        'update_form': edit_form,
#    }
#
#    return render(request, 'adminapp/user_update.html', content)

class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование пользователя"
        return context


#@user_passes_test(lambda u: u.is_superuser)
#def user_delete(request, pk):
#    title = 'пользователи/удаление'
#
#    user = get_object_or_404(ShopUser, pk=pk)
#
#    if request.method == 'POST':
#        user.is_active = False
#        user.save()
#        return HttpResponseRedirect(reverse('admin:users'))
#
#    content = {
#        'title': title,
#        'user_to_delete': user,
#    }
#
#    return render(request, 'adminapp/user_delete.html', content)

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('adminapp:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())



#@user_passes_test(lambda u: u.is_superuser)
#def categories(request):
#    title = 'admin/cat'
#
#    categories_list = ProductCategory.objects.all()
#
#    content = {
#        'title': title,
#        'objects': categories_list,
#    }
#
#    return render(request, 'adminapp/categories.html', content)


class ProductCategoriesView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#    pass

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование категории"
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#    pass


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование категории"
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#    pass


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


#@user_passes_test(lambda u: u.is_superuser)
#def products(request, pk):
#    title = 'admin/products'
#
#    category = get_object_or_404(ProductCategory, pk=pk)
#    products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#    content = {
#        'title': title,
#        'category': category,
#        'objects': products_list,
#    }
#
#    return render(request, 'adminapp/products.html', content)

class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['pk']).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список товаров категории"
        context['pk'] = self.kwargs['pk']
        return context

#@user_passes_test(lambda u: u.is_superuser)
#def product_create(request, pk):
#    title = 'admin/product_create'
#
#    if request.method == 'POST':
#        product_form = ProductCreate(request.POST, request.FILES)
#        if product_form.is_valid():
#            product_form.save()
#            return HttpResponseRedirect(reverse('admin:categories'))
#    else:
#        product_form = ProductCreate()
#
#    content = {
#        'title': title,
#        'update_form': product_form,
#    }
#
#    return render(request, 'adminapp/product_create.html', content)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_create.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductCreate


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список товаров категории"
        context['pk'] = self.kwargs['pk']
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#    title = 'admin/product'
#
#    product = get_object_or_404(Product, pk=pk)
#
#   content = {
#        'title': title,
#        'object': product,
#    }
#
#    return render(request, 'adminapp/product_read.html', content)

class ProductDetalView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Просмотр товара"
        return context


#@user_passes_test(lambda u: u.is_superuser)
#def product_update(request, pk):
#    title = 'admin/product_update'
#
#    edit_product = get_object_or_404(Product, pk=pk)
#    if request.method == "POST":
#        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#        if edit_form.is_valid():
#            edit_form.save()
#            return HttpResponseRedirect(reverse('admin:products', args=[edit_product.category.pk]))
#    else:
#
#        edit_form = ProductEditForm(instance=edit_product)
#
#    content = {
#        'title': title,
#        'update_form': edit_form,
#        'object': edit_product,
#    }
#
#    return render(request, 'adminapp/product_update.html', content)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:categories')
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование товара"
        return context


#@user_passes_test(lambda u: u.is_superuser)
#def product_delete(request, pk):
#    title = 'продукт/удаление'
#
#    product_del = get_object_or_404(Product, pk=pk)
#
#    if request.method == 'POST':
#        product_del.delete()
#        return HttpResponseRedirect(reverse('admin:categories'))
#
#    content = {
#        'title': title,
#        'object': product_del,
#    }
#
#    return render(request, 'adminapp/product_delete.html', content)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())
