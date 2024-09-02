from modelo.Usuario import Usuario


class Paciente(Usuario):
    def __init__(self, id, nome, idade, cpf, sexo, localidade, senha, sintomas):
        super().__init__(id, nome, idade, cpf, sexo, localidade, senha)
        self.sintomas = sintomas
