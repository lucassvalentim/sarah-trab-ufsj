from persistencia.Persistencia import Persistencia
from modelo.ProfissionalSaude import ProfissionalSaude
import sqlite3


class PersistenciaProfissionalSaude(Persistencia):
    def __init__(self, db_name):
        super().__init__(db_name)
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS ProfissionalSaude (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            sexo TEXT,
            localidade TEXT,
            senha TEXT,
            especializacao TEXT,
            crm TEXT UNIQUE NOT NULL,
            formacao TEXT,
            tempoAtividade INTEGER,
            convenios TEXT,
            precoConsulta REAL
        );
        """
        self.create_table(create_table_sql)

    def inserir_profissional(self, profissional: ProfissionalSaude):
        try:
            profissional.id = self.insert(
                'ProfissionalSaude',
                ['nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha', 'especializacao', 'crm', 'formacao', 'tempoAtividade', 'convenios', 'precoConsulta'],
                [profissional.nome, profissional.idade, profissional.cpf, profissional.sexo, profissional.localidade, profissional.senha, profissional.especializacao, profissional.crm, profissional.formacao, profissional.tempoAtividade, profissional.convenios, profissional.precoConsulta]
            )
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir profissional de saúde: {e}")
            return None

    def remover_profissional(self, id):
        condition = f"id = {id}"
        self.remove('ProfissionalSaude', condition)

    def modificar_profissional(self, id, updates):
        condition = f"id = {id}"
        self.update('ProfissionalSaude', updates, condition)

    def pesquisar_profissional_id(self, id):
        condition = f"id = {id}"
        rows = self.fetch('ProfissionalSaude', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha', 'especializacao', 'crm', 'formacao', 'tempoAtividade', 'convenios', 'precoConsulta'], condition)
        if rows:
            row = rows[0]
            return ProfissionalSaude(*row)

    def pesquisar_profissional_nome(self, nome):
        condition = f"nome LIKE '%{nome}%'"
        rows = self.fetch('ProfissionalSaude', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha', 'especializacao', 'crm', 'formacao', 'tempoAtividade', 'convenios', 'precoConsulta'], condition)
        return [ProfissionalSaude(*row) for row in rows]

    def carregar_profissionais(self):
        rows = self.fetch('ProfissionalSaude', ['id', 'nome', 'idade', 'cpf', 'sexo', 'localidade', 'senha', 'especializacao', 'crm', 'formacao', 'tempoAtividade', 'convenios', 'precoConsulta'])
        return [ProfissionalSaude(*row) for row in rows]
