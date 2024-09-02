from persistencia.Persistencia import Persistencia
from modelo.Paciente import Paciente
import sqlite3


class PersistenciaPaciente(Persistencia):
    def __init__(self, db_name):
        super().__init__(db_name)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Paciente (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            sexo TEXT,
            localidade TEXT,
            senha TEXT
        );
        """
        self.create_table(create_table_sql)

    def inserir_paciente(self, paciente: Paciente):
        try:
            paciente.id = self.insert(
                'Paciente',
                ['nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha'],
                [paciente.nome, paciente.idade, paciente.cpf, paciente.sexo, paciente.localidade, paciente.senha]
            )
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir paciente: {e}")
            return None

    def remover_paciente(self, id):
        condition = f"id = {id}"
        self.remove('Paciente', condition)

    def modificar_paciente(self, id, updates):
        condition = f"id = {id}"
        self.update('Paciente', updates, condition)

    def pesquisar_paciente_id(self, id):
        condition = f"id = {id}"
        rows = self.fetch('Paciente', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha'], condition)
        if rows:
            row = rows[0]
            return Paciente(*row)

    def pesquisar_paciente_nome(self, nome):
        condition = f"nome LIKE '%{nome}%'"
        rows = self.fetch('Paciente', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha'], condition)
        return [Paciente(*row) for row in rows]

    def carregar_pacientes(self):
        rows = self.fetch('Paciente', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha'])
        return [Paciente(*row) for row in rows]
