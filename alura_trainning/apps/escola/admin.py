from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


@admin.register(Aluno)
class AlunosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'rg',
        'cpf',
        'data_nascimento'
    )

    list_display_links = (
        'id',
        'nome'
    )

    search_fields = (
        'nome',
    )

    list_per_page = 20


@admin.register(Curso)
class CursosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo_curso',
        'descricao',
    )

    list_display_links = (
        'id',
        'codigo_curso'
    )

    search_fields = (
        'codigo_curso',
    )


@admin.register(Matricula)
class CursosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'aluno',
        'curso',
    )

    list_display_links = (
        'id',
        'aluno'
    )

    search_fields = (
        'aluno',
        'curso'
    )
