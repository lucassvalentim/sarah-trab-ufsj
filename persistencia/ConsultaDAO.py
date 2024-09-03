import sqlite3
from modelo.Consulta import Consulta
from persistencia.ProfissionalSaudeDAO import ProfissionalSaudeDAO
from persistencia.PacienteDAO import PacienteDAO
from datetime import datetime

from persistencia.Persistencia import Persistencia

class ConsultaDAO(Persistencia):
    def __init__(
            self, 
            db_name, 
            persistencia_paciente:PacienteDAO,
            persistencia_profissional: ProfissionalSaudeDAO):
        super().__init__(db_name)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Consulta (
            id INTEGER PRIMARY KEY,
            profissional_id INTEGER NOT NULL,
            paciente_id INTEGER NOT NULL,
            valor REAL NOT NULL,
            data_horario TEXT NOT NULL,
            FOREIGN KEY(profissional_id) REFERENCES ProfissionalSaude(id),
            FOREIGN KEY(paciente_id) REFERENCES Paciente(id)
        );
        """
        self.create_table(create_table_sql)
        self.ppa = persistencia_paciente
        self.pps = persistencia_profissional

    def inserir_consulta(self, consulta: Consulta):
        try:
            consulta.id = self.insert(
                'Consulta',
                ['profissional_id', 'paciente_id', 'valor', 'data_horario'],
                [consulta.profissional.id, consulta.paciente.id, consulta.valor, consulta.data_horario.isoformat()]
            )
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir consulta: {e}")
            return None

    def remover_consulta(self, id):
        condition = f"id = {id}"
        self.remove('Consulta', condition)

    def modificar_consulta(self, id, updates):
        if 'data_horario' in updates:
            updates['data_horario'] = updates['data_horario'].isoformat()
        condition = f"id = {id}"
        self.update('Consulta', updates, condition)

    def pesquisar_consulta_id(self, id):
        condition = f"id = {id}"
        rows = self.fetch('Consulta', ['id', 'profissional_id', 'paciente_id', 'valor', 'data_horario'], condition)
        if rows:
            row = rows[0]
            profissional = self.pesquisar_profissional_id(row[1])
            paciente = self.pesquisar_paciente_id(row[2])
            return Consulta(row[0], profissional, paciente, row[3], datetime.fromisoformat(row[4]))

    def carregar_consultas(self):
        rows = self.fetch('Consulta', ['id', 'profissional_id', 'paciente_id', 'valor', 'data_horario'])
        consultas = []
        for row in rows:
            profissional = self.pesquisar_profissional_id(row[1])
            paciente = self.pesquisar_paciente_id(row[2])
            consulta = Consulta(row[0], profissional, paciente, row[3], datetime.fromisoformat(row[4]))
            consultas.append(consulta)
        return consultas
    
    def pesquisar_profissional_id(self, id):
        return self.pps.pesquisar_profissional_id(id)

    def pesquisar_paciente_id(self, id):
        return self.ppa.pesquisar_paciente_id(id)

    def carregar_consultas_paciente(self, paciente_id):
        condition = f"paciente_id = {paciente_id}"
        rows = self.fetch('Consulta', ['id', 'profissional_id', 'paciente_id', 'valor', 'data_horario'], condition)
        consultas = []
        for row in rows:
            profissional = self.pesquisar_profissional_id(row[1])
            paciente = self.pesquisar_paciente_id(row[2])
            consulta = Consulta(row[0], profissional, paciente, row[3], datetime.fromisoformat(row[4]))
            consultas.append(consulta)
        return consultas

    def carregar_consultas_profissional(self, profissional_id):
        condition = f"profissional_id = {profissional_id}"
        rows = self.fetch('Consulta', ['id', 'profissional_id', 'paciente_id', 'valor', 'data_horario'], condition)
        consultas = []
        for row in rows:
            profissional = self.pesquisar_profissional_id(row[1])
            paciente = self.pesquisar_paciente_id(row[2])
            consulta = Consulta(row[0], profissional, paciente, row[3], datetime.fromisoformat(row[4]))
            consultas.append(consulta)
        return consultas