from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from teste_api.models import Ingresso
from django.utils import timezone


# Create your views here.
def validador(request):
    if request.method == 'GET':
        ingressos = Ingresso.objects.filter(validado=False)
        return render(request, 'validador/validador.html', {'ingressos': ingressos, 'title': 'Validador'})

    elif request.method == 'POST':

        try:
            codigos_ingressos = request.POST.getlist('ingressos_selecionados')

            try:
                for ingresso in codigos_ingressos:
                    Ingresso.objects.filter(id=ingresso).update(validado=True)

                return JsonResponse({'sucesso': True,
                                     'status': 'Ingressos validados com sucesso!',
                                     'ingressos_validados': codigos_ingressos})
            except:
                ingressos_validados = [Ingresso.objects.get(validado=True, id=codigo) for codigo in codigos_ingressos]
                ingressos_erro = [Ingresso.objects.get(validado=False, id=codigo) for codigo in codigos_ingressos]
                return JsonResponse({'sucesso': True,
                                     'status': 'Erro ao validar ingressos',
                                     'ingressos_validados': ingressos_validados,
                                     'ingressos_erro': ingressos_erro})
        except Exception as e:
            return JsonResponse({'sucesso': False,
                                 'status': 'Erro ao tentar validar ingressos'})