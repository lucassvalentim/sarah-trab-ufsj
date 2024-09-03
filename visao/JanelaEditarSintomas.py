from tkinter import *
import tkinter
from visao.JanelaPadrao import JanelaPadrao
from visao.JanelaErro import JanelaErro
from controle.ControleProblema import ControleProblema


class JanelaEditarSintomas(JanelaPadrao):
    def __init__(self, master, cpf, controleproblema: ControleProblema):
        super().__init__(master)

        self.cpf_valor = cpf
        self.id = 0
        self.controleproblema = controleproblema

        # INICIALIZANDO OS ATRIBUTOS DA TELA
        self.secondary_window = tkinter.Toplevel()
        self.secondary_window.resizable(0, 0)
        self.secondary_window.title("Editar Sintomas")
        self.secondary_window.config(width=300, height=170, bg=self.sidebar_color)

        # INICIALIZANDO A CONFIGURAÇÃO DOS CONTAINERS COM AS INFORMAÇÕES
        self.container_sintomas = tkinter.Frame(self.secondary_window, bg=self.sidebar_color)
        self.container_sintomas.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.7)

        self.editarsintomas()

    def editarsintomas(self):

        label_sintomas = tkinter.Label(self.container_sintomas, text='Editar sintomas:', font=self.fonte)
        label_sintomas.pack(padx=15, pady=5, anchor='center')
        self.entry_sintomas = tkinter.Entry(self.container_sintomas, font=self.fonte_menor, width=40)
        self.entry_sintomas.pack(padx=20, pady=5)

        botao_registrar = tkinter.Button(self.secondary_window, text='Alterar', font=self.fonte_menor,
                                         bg=self.sidebar_color, command=self.alterarsintomas)
        botao_registrar.place(relx=0.8, rely=0.80, anchor=CENTER, width=100, height=30)

    def alterarsintomas(self):
        sintomas_novos = self.entry_sintomas.get()

        if not sintomas_novos:
            button_open = tkinter.Button(
                self.master,
                text="Informações invalidas",
                command=self.JanelaSecundaria()
            )
        else:
            row = self.controleproblema.carregar()
            print(self.cpf_valor)
            for info in row:
                if self.cpf_valor == info.cpf:
                    self.id = info.id
                    print(id)
                    break

            dados = {
                "sintomas": sintomas_novos
            }

            self.controleproblema.modificar(self.id, dados)
            self.excluirjanela()

    def JanelaSecundaria(self):
        JanelaErro(self.master)

    def excluirjanela(self):
        self.secondary_window.destroy()
