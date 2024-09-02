import tkinter
from tkinter import ttk
from visao.JanelaPadrao import JanelaPadrao


# ESSA CLASSE SERVE PARA CRIAR A JANELA DE ERRO
class JanelaExcluirInformacoes(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.sidebar_color = '#CFCFCF'
        self.selectionbar_color = '#eff5f6'

        self.JanelaDeletar()

    def JanelaDeletar(self):
        secondary_window = tkinter.Toplevel()
        secondary_window.resizable(0, 0)
        secondary_window.title("Excluir Informações")
        secondary_window.config(width=250, height=170, bg=self.sidebar_color)
        # BOTAO PARA DESTRUIR ESSA JANELA
        button_close = tkinter.Button(
            secondary_window,
            text="Perfil excluído com sucesso!",
            font=self.fonte_menor,
            command=self.fechar_janelas,
            bg=self.selectionbar_color

        )
        button_close.place(x=20, y=60)

    def fechar_janelas(self):
        self.master.destroy()
