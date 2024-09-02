from modelo.Problema import Problema

class ControleProblema:

    def __init__(self, persistencia):
        self.persistencia = persistencia

    def modificar(self, id, modificacoes):
        self.persistencia.modificar_problema(id, modificacoes)

    def remover(self, id):
        self.persistencia.remover_problema(id)

    def inserir(self, problema: Problema):
        self.persistencia.inserir_problema(problema)

    def pesquisar(self, sintomas=None, cpf=None, id=None):
        if id is not None:
            return self.persistencia.pesquisar_problema_id(id)
        elif sintomas is not None:
            return self.persistencia.pesquisar_problema_nome(sintomas)
        elif cpf is not None:
            condition = f"cpf = '{cpf}'"
            rows = self.persistencia.fetch('Problema', ['id', 'cpf', 'sintomas'], condition)
            if rows:
                row = rows[0]
                return Problema(*row)
        return None

    def carregar(self):
        return self.persistencia.carregar_problema()
