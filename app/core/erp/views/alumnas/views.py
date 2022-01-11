from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from datetime import datetime
from django.core import serializers

from core.erp.forms import AlumnasForm
from core.erp.models import Alumnas

# def StudentDelete(self, request):
'''
def student_delete(request):
    data = {}
    try:
        data['error'] = "WORKING!"
        #self.get_object()
        #self.object.delete()
    except Exception as e:
        data['error'] = str(e)
    return HttpResponse('success')
    #return JsonResponse(data)
'''


def birthdays_get_list_ajax(request):
    if request.method == 'GET':
        data = {}
        try:
            students = Alumnas.objects.filter(date_of_birth__month=datetime.now().month, date_of_birth__day=datetime.now().day)
            data = {}
            '''
            json_list = []
            for student in students:
                json_dict = model_to_dict(student)
                json_list.append(json_dict)
            # data['error'] = 'TIENE EL ATRIBUTO ERROR'
            data['json_list'] = json_list
            '''
            ids = []
            names = []
            surnames = []
            ages = []

            for student in students:
                ids.append(student.id)
                names.append(student.names)
                surnames.append(student.surnames)
                ages.append(datetime.now().year - student.date_of_birth.year)
            data['ids'] = ids
            data['names'] = names
            data['surnames'] = surnames
            data['ages'] = ages
            #h = 1/0
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


def alumnas_borrar_ajax(request):
    if request.method == 'GET':
        data = {}
        id = request.GET['id']
        # data = {'id': id}
        try:
            c = Alumnas.objects.get(pk=id)
            # c = Alumnas.objects.get(pk=2567)
            c.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        # return HttpResponse('success')


class AlumnasListView(ListView):
    model = Alumnas
    template_name = 'alumnas/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Alumnas.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de alumnas'
        context['create_url'] = reverse_lazy('erp:alumnas_crear')
        context['list_url'] = reverse_lazy('erp:alumnas_listado')
        context['entity'] = 'Alumnas'
        return context


class AlumnasCreateView(CreateView):
    model = Alumnas
    form_class = AlumnasForm
    template_name = 'alumnas/create.html'
    success_url = reverse_lazy('erp:alumnas_listado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ingreso de una alumna nueva'
        context['list_url'] = reverse_lazy('erp:alumnas_listado')
        context['entity'] = 'Alumnas'
        context['action'] = 'add'
        return context


class AlumnasUpdateView(UpdateView):
    model = Alumnas
    form_class = AlumnasForm
    template_name = 'alumnas/create.html'
    success_url = reverse_lazy('erp:alumnas_listado')

    '''
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una alumna'
        context['list_url'] = reverse_lazy('erp:alumnas_listado')
        context['entity'] = 'Alumnas'
        context['action'] = 'edit'
        context['checked_goals'] = self.get_object().goals
        return context
