from django.db import models

class TravelPackage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço Original')
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço com Desconto')
    image = models.ImageField(upload_to='travel_packages/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de Edição')

    class Meta:
        db_table = 'travel_packages'

    def __str__(self):
        return self.name
