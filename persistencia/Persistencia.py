import sqlite3


class Persistencia:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self, create_table_sql):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)

    def insert(self, table, columns, values):
        with self.connect() as conn:
            cursor = conn.cursor()
            placeholders = ', '.join(['?'] * len(values))
            sql = f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({placeholders})'
            cursor.execute(sql, values)
            conn.commit()
            return cursor.lastrowid

    def remove(self, table, condition):
        with self.connect() as conn:
            cursor = conn.cursor()
            sql = f'DELETE FROM {table} WHERE {condition}'
            cursor.execute(sql)
            conn.commit()

    def update(self, table, updates, condition):
        with self.connect() as conn:
            cursor = conn.cursor()
            set_clause = ', '.join([f'{col} = ?' for col in updates.keys()])
            sql = f'UPDATE {table} SET {set_clause} WHERE {condition}'
            cursor.execute(sql, list(updates.values()))
            conn.commit()

    def fetch(self, table, columns, condition=None):
        with self.connect() as conn:
            cursor = conn.cursor()
            sql = f'SELECT {", ".join(columns)} FROM {table}'
            if condition:
                sql += f' WHERE {condition}'
            cursor.execute(sql)
            return cursor.fetchall()
