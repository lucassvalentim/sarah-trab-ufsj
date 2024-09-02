from persistencia.Persistencia import Persistencia
from modelo.Problema import Problema
import sqlite3


class PersistenciaProblema(Persistencia):
    def __init__(self, db_name):
        super().__init__(db_name)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS Problema (
            id INTEGER PRIMARY KEY,
            cpf TEXT UNIQUE NOT NULL,
            sintomas TEXT
        );
        """
        self.create_table(create_table_sql)

    def inserir_problema(self, problema: Problema):
        try:
            problema.id = self.insert(
                'Problema',
                ['cpf', 'sintomas'],
                [problema.cpf, problema.sintomas]
            )
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir problema: {e}")
            return None

    def remover_problema(self, id):
        condition = f"id = {id}"
        self.remove('Problema', condition)

    def modificar_problema(self, id, updates):
        condition = f"id = {id}"
        self.update('Problema', updates, condition)

    def pesquisar_problema_id(self, id):
        condition = f"id = {id}"
        rows = self.fetch('Problema', ['id', 'cpf', 'sintomas'], condition)
        if rows:
            row = rows[0]
            return Problema(*row)

    def pesquisar_problema_nome(self, nome):
        condition = f"nome LIKE '%{nome}%'"
        rows = self.fetch('Problema', ['id', 'cpf', 'sintomas'], condition)
        return [Problema(*row) for row in rows]

    def carregar_problema(self):
        rows = self.fetch('Problema', ['id', 'cpf', 'sintomas'])
        return [Problema(*row) for row in rows]
