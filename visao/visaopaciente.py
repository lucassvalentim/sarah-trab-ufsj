from modelo.Paciente import Paciente
from controle.ControlePaciente import ControlePaciente


class Visaopaciente:
    def __init__(self, controle:ControlePaciente):
        self.controle = controle

    def inserir(
            self,
            nome,
            idade,
            cpf,
            sexo,
            localidade,
            senha,
            sintomas):

        paciente = Paciente(
            0,
            nome,
            idade,
            cpf,
            sexo,
            localidade,
            senha,
            sintomas
            )

        self.controle.inserir(paciente)

    def vizualizar(self):
        pass

    def deletar(self, id):
        self.controle.remover(id)
