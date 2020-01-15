from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Subdivision, Project
from .forms import SubdivisionForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.urls import reverse_lazy

"""
1. Страница добавления, удаления подразделения
   Управление участниками
2. Блок с обычными пользователями
3. Страница создания, удаления, просмотра, изменения, проекта
4. RestApi для страниц

Модель валидации создается либо с forms.Form без привязки к модели бд
или ModelForm с моделью бд и засовывается в generic.edit View, в аттрибут form_class

"""
def index(request):
    return render(request, 'list_groups.html')

class SubdivisionListView(ListView):
    model = Subdivision
    template_name = 'subdivision_list.html'
    context_object_name = 'subdivision_list'   # ваше собственное имя переменной контекста в шаблоне
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some_data'] = 'в get_context_data передавать свои параметры'
        return context

#    def get_queryset(self):
#        return Subdivision.objects.filter(title__icontains='люди')[:5] 


class SubdivisionCreate(CreateView):
    model = Subdivision
    template_name = 'subdivision_form.html'#fields = [ 'title', 'description', 'participants' ]
    form_class = SubdivisionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some_data'] = 'в get_context_data передавать свои параметры'
        return context


class SubdivisionDetailView(DetailView):
    model = Subdivision
    template_name = 'subdivision_detail.html'


class SubdivisionUpdate(UpdateView):
    model = Subdivision
    template_name = 'subdivision_form.html'#fields = ['title', 'description' ]
    form_class = SubdivisionForm

class SubdivisionDelete(DeleteView):
    model = Subdivision
    template_name = 'subdivision_form.html'
    success_url = reverse_lazy('subdivision_list')



