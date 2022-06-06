from django.urls import path
from .views import AdocaoDetail, AdocaoList

urlpatterns = [
    path('', AdocaoList.as_view()), # vai usar api/adocoes e transformar a api view em view
    path('cadastro/', AdocaoDetail.as_view()) # vai usar api/adocoes e transformar a api view em view
]