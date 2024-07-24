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

    def exibirDados(self):
        print(f"Id: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\n"
              f"Cpf: {self.cpf}\nSexo: {self.sexo}\nLocalidade: {self.localidade}\n"
              f"Especialização: {self.especializacao}\nCrm: {self.crm}\nFormacao: {self.formacao}\n"
              f"TempoAtividade: {self.tempoAtividade}\nConvenios: {self.convenios}\nPreço Consulta: {self.precoConsulta}\n")