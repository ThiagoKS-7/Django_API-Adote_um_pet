from django.db import models

class Adocao(models.Model):
    valor = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2) # sem null, sem vazio, 5 num, 2 decimal (999.99)
    email = models.EmailField(blank=False, null=False, max_length=255)
    pet = models.ForeignKey(to='pet.Pet', null=False, on_delete=models.CASCADE) # ADOCAO DEPENDE DE PET, PRECISA DE FOREIGN KEY PRA ELE