import sqlite3
from modelo.Agendamento import Agendamento
from persistencia.Persistencia import Persistencia
from datetime import datetime


class PersistenciaAgendamento(Persistencia):
    def __init__(self, db_name):
        super().__init__(db_name)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Agendamento (
            id INTEGER PRIMARY KEY,
            paciente_id INTEGER NOT NULL,
            profissional_id INTEGER NOT NULL,
            data_horario TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY(paciente_id) REFERENCES Paciente(id),
            FOREIGN KEY(profissional_id) REFERENCES ProfissionalSaude(id)
        );
        """
        self.create_table(create_table_sql)

    def inserir_agendamento(self, agendamento: Agendamento):
        try:
            agendamento.id = self.insert(
                'Agendamento',
                ['paciente', 'profissional', 'data_horario', 'status'],
                [agendamento.paciente, agendamento.profissional, agendamento.data_horario.isoformat(), agendamento.status]
            )
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir agendamento: {e}")
            return None

    def remover_agendamento(self, id):
        condition = f"id = {id}"
        self.remove('Agendamento', condition)

    def modificar_agendamento(self, id, updates):
        if 'data_horario' in updates:
            updates['data_horario'] = updates['data_horario'].isoformat()
        condition = f"id = {id}"
        self.update('Agendamento', updates, condition)

    def pesquisar_agendamento_id(self, id):
        condition = f"id = {id}"
        rows = self.fetch('Agendamento', ['id', 'paciente_id', 'profissional_id', 'data_horario', 'status'], condition)
        if rows:
            row = rows[0]
            return Agendamento(row[0], row[1], row[2], datetime.fromisoformat(row[3]), row[4])
        
    def carregar_agendamentos(self):
        rows = self.fetch('Agendamento', ['id', 'paciente_id', 'profissional_id', 'data_horario', 'status'])
        return [Agendamento(row[0], row[1], row[2], datetime.fromisoformat(row[3]), row[4]) for row in rows]
    
    def salvar(self, agendamento):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Agendamentos (paciente_id, profissional_id, data_horario)
                VALUES (?, ?, ?)
            """, (agendamento['paciente_id'], agendamento['profissional_id'], agendamento['data_horario'].isoformat()))
            conn.commit()