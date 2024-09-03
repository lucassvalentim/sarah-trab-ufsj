from modelo.Agendamento import Agendamento
from persistencia.PersistenciaAgendamento import PersistenciaAgendamento
from datetime import datetime


class ControleAgendamento:
    def __init__(self, persistencia: PersistenciaAgendamento):
        self.persistencia = persistencia

    def inserir(self, agendamento:Agendamento):
        self.persistencia.inserir_agendamento(agendamento)

    def modificar(self, id, modificacoes):
        if 'data_horario' in modificacoes and isinstance(modificacoes['data_horario'], str):
            modificacoes['data_horario'] = datetime.fromisoformat(modificacoes['data_horario'])
        self.persistencia.modificar_agendamento(id, modificacoes)

    def remover(self, id):
        self.persistencia.remover_agendamento(id)

    def pesquisar(self, id=None):
        if id is not None:
            return self.persistencia.pesquisar_agendamento_id(id)
        return None

    def carregar(self):
        return self.persistencia.carregar_agendamentos()
