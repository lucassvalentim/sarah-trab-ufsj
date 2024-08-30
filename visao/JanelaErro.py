import tkinter
from tkinter import ttk
from visao.JanelaPadrao import JanelaPadrao

# ESSA CLASSE SERVE PARA CRIAR A JANELA DE ERRO
class JanelaErro(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.sidebar_color = '#CFCFCF'
        self.selectionbar_color = '#eff5f6'

        self.JanelaSecundaria()

    def JanelaSecundaria(self):
        secondary_window = tkinter.Toplevel()
        secondary_window.resizable(0,0)
        secondary_window.title("Erro")
        secondary_window.config(width=200, height=170, bg=self.sidebar_color)
        # BOTAO PARA DESTRUIR ESSA JANELA
        button_close = tkinter.Button(
            secondary_window,
            text="Informações inválidas!",
            font=self.fonte_menor,
            command=secondary_window.destroy,
            bg=self.selectionbar_color

        )
        button_close.place(x=20, y=60)
