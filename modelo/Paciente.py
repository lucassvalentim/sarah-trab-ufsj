from modelo.Usuario import Usuario

class Paciente(Usuario):
    def __init__(self, id, nome, idade, cpf, sexo, localidade):
        super().__init__(id, nome, idade, cpf, sexo, localidade)

    def exibirDados(self):
        print(f"Id: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\n"
              f"Cpf: {self.cpf}\nSexo: {self.sexo}\nLocalidade: {self.localidade}\n")