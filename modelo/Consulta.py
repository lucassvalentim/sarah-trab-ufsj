from modelo.Objeto import Objeto
from modelo.Paciente import Paciente
from modelo.ProfissionalSaude import ProfissionalSaude
from datetime import datetime

class Consulta(Objeto):
    
    def __init__(self, id: int, profissional: ProfissionalSaude, paciente: Paciente, valor: float, data_horario: str):
        super().__init__(id)
        self.profissional = profissional
        self.paciente = paciente
        self.valor = valor
        self.data_horario = data_horario
    