from django.db import models
import os

class TravelPackage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço Original')
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço com Desconto')
    image = models.ImageField(upload_to='travel_packages/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de Edição')

    class Meta:
        db_table = 'travel_packages'
        verbose_name = 'Pacote De Viagem'
        verbose_name_plural = 'Pacotes De Viagens'

    def save(self, *args, **kwargs):
        # Verificar se o objeto já existe no banco de dados
        if self.pk:
            # Buscar o objeto atual do banco
            old_image = TravelPackage.objects.get(pk=self.pk).image
            # Comparar se a imagem foi alterada
            if old_image and old_image != self.image:
                # Remover a imagem antiga do sistema de arquivos
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        super().save(*args, **kwargs)  # Salvar o novo registro      

        #subescrever o metodo delete para remover a imagem
        def delete(self, *args, **kwargs):
            #remover a imagem associada ao objeto
            if self.image and os.path.isfile(self.image.path):
                os.remove(self.image.path)
            super().delete(*args, **kwargs) #excluir o registro          

    def __str__(self):
        return self.name

