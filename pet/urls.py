from django.urls import path
from .views import PetList, PetDetail

urlpatterns = [
    path("", PetList.as_view()),  # vai usar api/pets e transformar a api view em view
    path("cadastro/", PetDetail.as_view()),
]
