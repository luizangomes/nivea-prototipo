"""Acabou não sendo usada. Dava pra usar fácil, inclusive devia mas percebi meio tarde só"""
class Aluno:
    def __init__(self, nome="", ano=0, turma="", relatorios={}):
        self.nome = nome
        self.ano = ano
        self.turma = turma
        self.relatorios = relatorios

aluno = Aluno()
print(aluno.nome)