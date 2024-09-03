from modelo.Consulta import Consulta
from datetime import datetime
from persistencia.ConsultaDAO import ConsultaDAO
from modelo.Paciente import Paciente

class ControleConsulta:

    def __init__(self, persistencia:ConsultaDAO):
        self.persistencia = persistencia

    def modificar(self, id, modificacoes):
        if 'data_horario' in modificacoes and isinstance(modificacoes['data_horario'], str):
            modificacoes['data_horario'] = datetime.fromisoformat(modificacoes['data_horario'])
        self.persistencia.modificar_consulta(id, modificacoes)

    def remover(self, id):
        self.persistencia.remover_consulta(id)

    def inserir(self, consulta: Consulta):
        self.persistencia.inserir_consulta(consulta)

    def pesquisar(self, id_consulta=None, id_medico=None):
        if id_consulta is not None:
            return self.persistencia.pesquisar_consulta_id(id_consulta)
        if id_medico is not None:
            return self.persistencia.pesquisar_profissional_id(id_medico)
        return None

    def carregar(self):
        return self.persistencia.carregar_consultas()

    def carregar_por_paciente(self, paciente_id):
        return self.persistencia.carregar_consultas_paciente(paciente_id)

    def carregar_por_profissional(self, profissional_id):
        return self.persistencia.carregar_consultas_profissional(profissional_id)