from modelo.Problema import Problema
from controle.ControleProblema import ControleProblema


class Visaoproblema:
    def __init__(self, controle:ControleProblema):
        self.controle = controle

    def inserir(
            self,
            cpf,
            sintomas
            ):

        problema = Problema(
            0,
            cpf,
            sintomas
            )

        self.controle.inserir(problema)

    def vizualizar(self):
        pass

    def deletar(self, id):
        self.controle.remover(id)
