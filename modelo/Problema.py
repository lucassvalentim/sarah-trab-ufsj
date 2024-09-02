from modelo.Objeto import Objeto
from modelo.Paciente import Paciente

class Problema(Objeto):

    def __init__(self, id: int, cpf, sintomas):
        super().__init__(id)
        self.cpf = cpf
        self.sintomas = sintomas
