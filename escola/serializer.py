from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

# aqui é a ponte da nossa api
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
      model = Curso
      fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
        # pega todos menos o id
        # exclude = ['id']


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    # curso é do tipo de leitura e sera representado pela sua descricao
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    # visualizar o que ta escrito no campo e nao o M, V, N | para isso deve se criar uma def
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']


    def get_periodo(self, obj):
        # vai mostrar do mesmo jeito que mostra no django admin
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    # pegando o nome do aluno
    aluno_nome = serializers.ReadOnlyField(source = 'aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']


