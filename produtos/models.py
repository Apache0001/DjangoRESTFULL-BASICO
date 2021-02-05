from django.db import models

# Create your models here.


class Base(models.Model):
    data_publicacao =  models.DateField(auto_now_add = True)
    data_atualizacao = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract =  True

class Produto(Base):
    titulo = models.CharField(max_length=300)
    descricao = models.CharField(max_length=1000)
    categoria = models.TextField(max_length=100)
    especificacoes = models.TextField(max_length=2000)
    preco =  models.DecimalField(max_digits=7, decimal_places=2)
    desconto = models.DecimalField(max_digits=4, decimal_places=2)
    url = models.URLField(unique=True, max_length=255)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.titulo

class Avaliacao(Base):
    produto = models.ForeignKey(Produto, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'produto']

    def __str__(self):
        return f"{self.nome} avaliou o curso {self.produto} com nota {self.avaliacao}"