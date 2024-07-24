from tkinter import *
from tkinter import messagebox


class JanelaPadrao:
    def __init__(self, master=None):
        self.master = master
        self.configurarJanela()

    def configurarJanela(self):
        self.master.title("SARAH - Sistema de Apoio e Recursos "
                          "em Assistência a Saúde e Hospitalar.")

        self.master.geometry("1080x620")
        self.master.configure(background="white")
        self.master.resizable(width=False, height=False)
