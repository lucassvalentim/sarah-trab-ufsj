from modelo.Objeto import Objeto


class Usuario(Objeto):
    def __init__(self, id, nome, idade, cpf, sexo, localidade):
        super().__init__(id)
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sexo = sexo
        self.localidade = localidade