"""adote_um_pet URL Configuration

Examples:
**Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

**Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

'''URLPATTERNS GERAL FICA SÓ COM O ADMIN E COM O PATH PRINCIPAL DE CADA APP'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pets/', include('pet.urls')), # inclui tudo que tiver dentro da urlpatters do app pet
    path('api/adocoes/', include('adocao.urls'))
]
