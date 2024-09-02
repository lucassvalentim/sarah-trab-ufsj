from modelo.ProfissionalSaude import ProfissionalSaude

class ControleProfissionalSaude:

    def __init__(self, persistencia):
        self.persistencia = persistencia

    def modificar(self, id, modificacoes):
        self.persistencia.modificar_profissional(id, modificacoes)

    def remover(self, id):
        self.persistencia.remover_profissional(id)

    def inserir(self, profissional: ProfissionalSaude):
        self.persistencia.inserir_profissional(profissional)

    def pesquisar(self, nome=None, cpf=None, crm=None, id=None):
        if id is not None:
            return self.persistencia.pesquisar_profissional_id(id)
        elif nome is not None:
            return self.persistencia.pesquisar_profissional_nome(nome)
        elif cpf is not None:
            condition = f"cpf = '{cpf}'"
            rows = self.persistencia.fetch('ProfissionalSaude', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha', 'especializacao', 'crm', 'formacao', 'tempoAtividade', 'convenios', 'precoConsulta'], condition)
            if rows:
                row = rows[0]
                return ProfissionalSaude(*row)
        elif crm is not None:
            condition = f"crm = '{crm}'"
            rows = self.persistencia.fetch('ProfissionalSaude', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha', 'especializacao', 'crm', 'formacao', 'tempoAtividade', 'convenios', 'precoConsulta'], condition)
            if rows:
                row = rows[0]
                return ProfissionalSaude(*row)
        return None

    def carregar(self):
        return self.persistencia.carregar_profissionais()
