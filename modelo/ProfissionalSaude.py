from modelo.Usuario import Usuario

class ProfissionalSaude(Usuario):
    def __init__(self, id, nome, idade, cpf, sexo, localidade, especializacao, crm,
                 formacao, tempoAtividade, convenios, precoConsulta):
        super().__init__(id, nome, idade, cpf, sexo, localidade)
        self.especializacao = especializacao
        self.crm = crm
        self.formacao = formacao
        self.tempoAtividade = tempoAtividade
        self.convenios = convenios
        self.precoConsulta = precoConsulta