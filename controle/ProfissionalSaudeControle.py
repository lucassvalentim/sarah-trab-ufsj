from controle.Controle import Controle
from modelo.Usuario import Usuario


class ProfissionalSaudeControle(Controle):

    def __int__(self, persistencia):
        super().__int__(persistencia)

    def salvar(self, objeto: Usuario):
        pass

    def modificar(self, objeto: Usuario):
        pass

    def remover(self, objeto: Usuario):
        pass

    def inserir(self, objeto: Usuario):
        pass

    def pesquisar(self, objeto: Usuario):
        pass

    def carregar(self, objeto: Usuario):
        pass
