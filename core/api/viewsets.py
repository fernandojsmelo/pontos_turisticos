from django.http import HttpResponse
# from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing pontoturistico
    """
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    # permission_classes = (DjangoModelPermissions,)
    # authentication_classes = (TokenAuthentication,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get(('id', None))
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        # return PontoTuristico.objects.filter(aprovado=True)

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = PontoTuristico.objects.filter(nome=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def denuciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()

        return HttpResponse('OK')