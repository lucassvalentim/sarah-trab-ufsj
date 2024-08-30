import tkinter
from tkinter import *
from visao.JanelaPadrao import JanelaPadrao


class JanelaContainerMedico(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)

        # INICIALIZA OS ATRIBUTOS FIXOS DA TELA

        # INICIALIZANDO A CONFIGURAÇÃO DOS FRAMES RESPONSÁVEIS POR MOSTRAR OS CARDS DOS PACIENTES OU
        # MÉDICOS
        self.container = tkinter.Frame(self.master, bg=self.sidebar_color)
        self.container.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.6)

        self.telapaciente()

    # FUNÇÃO RESPONSÁVEL POR MOSTRAR AS INFORMAÇÕES DO PACIENTE PARA O MÉDICO
    def telapaciente(self):
        # IMAGEM MEDICO
        img_user = tkinter.PhotoImage(file='/home/izzy/sarah-trab-ufsj/assets/flor.png')
        self.master.iconphoto(True, img_user)

        nome_user = img_user.subsample(1)
        logo = tkinter.Label(self.container, image=nome_user, bg=self.img_color, anchor=CENTER)
        logo.place(x=10, y=20)

        # NOME MEDICO
        img_name = tkinter.Label(self.container, text='Nome: ' + 'Flor', bg=self.sidebar_color, font=self.fonte_menor)
        img_name.place(x=220, y=25, anchor="w")

        # CARACTERISTICAS MEDICO
        idade_usuario = tkinter.Label(self.container, text='Idade: ' + '20', bg=self.sidebar_color,
                                      font=self.fonte_menor)
        idade_usuario.place(x=220, y=50, anchor="w")

        sintomas = 'Dor de cabeça constante. Febre e náuseas.'
        sintomas_usuario = tkinter.Label(self.container, text=sintomas, bg=self.sidebar_color,
                                         font=self.fonte_menor)
        sintomas_usuario.place(x=220, y=75, anchor="w")

        # BOTÃO PROXIMO
        next_button = tkinter.Button(self.container, text='Próximo', height=1, width=5, bg=self.selectionbar_color,
                                     command=self.botaoproxpressionado)
        next_button.place(x=470, y=270)

        # BOTÃO ACEITAR A CONSULTA
        botao_aceitar = tkinter.Button(self.container, text='Aceitar', height=1, width=5, bg=self.selectionbar_color)
        botao_aceitar.place(x=250, y=270)
    def botaoproxpressionado(self):

        # SELF.VAR SERVE PARA TROCAR DE TELAS QUANDO CLICADO EM PRÓXIMO
        # TODO: implementar lógica para troca de telas

        anterior_button = tkinter.Button(self.container, text='Anterior', height=1, width=5,
                                             bg=self.selectionbar_color,
                                             command=self.botaoproxpressionado)
        anterior_button.place(x=50, y=270)




