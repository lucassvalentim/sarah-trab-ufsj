from modelo.Usuario import Usuario
from modelo.Paciente import Paciente
from modelo.ProfissionalSaude import ProfissionalSaude
from datetime import datetime

class Agendamento(Usuario):
    def __init__(self, id: int, paciente: Paciente, profissional: ProfissionalSaude, data_horario: datetime, status="Agendado"):
        self.id = id
        self.paciente = paciente
        self.profissional = profissional
        self.data_horario = data_horario
        self.status = status
