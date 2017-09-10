from django.views.generic.edit import FormView
from app.forms import ProfileModelForm
from django.http import JsonResponse, HttpResponseBadRequest
import json


class AppFormView(FormView):
    template_name = 'app/index.html'
    form_class = ProfileModelForm
    initial = {
        'first_name': 'Test',
        'last_name': 'Testerov',
        'phone': '9999999999',
        'email': 'test@test.test',
        'birthday': '11.11.2011',
    }

    def form_valid(self, form):
        form.save()
        data = {
            'response': 'Данные успешно отправлены!!!',
            'result': 'success'
        }
        return JsonResponse(data)

    def form_invalid(self, form):
        response = {}
        for k in form.errors:
            response[k] = form.errors
        data = {
            'response': response,
            'result': 'error'
        }
        return JsonResponse(data)

