from modelo.Paciente import Paciente

class ControlePaciente:

    def __init__(self, persistencia):
        self.persistencia = persistencia

    def modificar(self, id, modificacoes):
        self.persistencia.modificar_paciente(id, modificacoes)

    def remover(self, id):
        self.persistencia.remover_paciente(id)

    def inserir(self, paciente: Paciente):
        self.persistencia.inserir_paciente(paciente)

    def pesquisar(self, nome=None, cpf=None, id=None):
        if id is not None:
            return self.persistencia.pesquisar_paciente_id(id)
        elif nome is not None:
            return self.persistencia.pesquisar_paciente_nome(nome)
        elif cpf is not None:
            condition = f"cpf = '{cpf}'"
            rows = self.persistencia.fetch('Paciente', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha', 'sintomas'], condition)
            if rows:
                row = rows[0]
                return Paciente(*row)
        return None

    def carregar(self):
        return self.persistencia.carregar_pacientes()
