from modelo.ProfissionalSaude import ProfissionalSaude
from controle.ControleProfissionalSaude import ControleProfissionalSaude


class VisaoProfissionalSaude:
    def __init__(self, controle:ControleProfissionalSaude):
        self.controle = controle

    def inserir(
            self,
            nome,
            idade,
            cpf,
            sexo,
            localidade,
            especializacao,
            crm,
            formacao,
            tempoAtividade,
            convenios,
            precoConsulta):

        profissional = ProfissionalSaude(
            0,
            nome,
            idade,
            cpf,
            sexo,
            localidade,
            especializacao,
            crm,
            formacao,
            tempoAtividade,
            convenios,
            precoConsulta)

        self.controle.inserir(profissional)

    def vizualizar(self):
        pass

    def deletar(self):
        pass
