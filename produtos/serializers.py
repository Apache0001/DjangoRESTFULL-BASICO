from rest_framework import serializers

from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_karg ={
            'email':{'write_only':True}
        }
        model = Produto
        fields = [
            'id',
            'titulo', 
            'descricao',
            'categoria',
            'especificacoes',
            'preco',
            'desconto',
            'url',
            'data_atualizacao',
            'data_publicacao',
            'ativo',
        ]