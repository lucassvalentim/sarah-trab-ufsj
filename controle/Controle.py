from persistencia.Persistencia import Persistencia
from modelo.Usuario import Usuario


class Controle(Persistencia):

    def __int__(self, persistencia):
        self.persistencia = persistencia

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
