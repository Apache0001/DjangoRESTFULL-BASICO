# Generated by Django 3.1.6 on 2021-02-05 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_publicacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=300)),
                ('descricao', models.CharField(max_length=1000)),
                ('categoria', models.CharField(max_length=100)),
                ('especificacoes', models.CharField(max_length=2000)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=4)),
                ('url', models.URLField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_publicacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comentario', models.TextField(blank=True, default='')),
                ('avaliacao', models.DecimalField(decimal_places=1, max_digits=2)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='produtos.produto')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
                'unique_together': {('email', 'produto')},
            },
        ),
    ]