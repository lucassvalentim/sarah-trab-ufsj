import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from visao.JanelaPadrao import JanelaPadrao
from visao.JanelaErro import JanelaErro
from visao.JanelaHomePaciente import JanelaHomePaciente
from visao.visaopaciente import Visaopaciente
from controle.ControlePaciente import ControlePaciente
from persistencia.PersistenciaPaciente import PersistenciaPaciente
from visao.visaoprofissional import Visaoprofissional
from controle.ControleProfissionalSaude import ControleProfissionalSaude
from persistencia.PersistenciaProfissionalSaude import PersistenciaProfissionalSaude
from persistencia.PersistenciaProblema import PersistenciaProblema
from controle.ControleProblema import ControleProblema
from visao.visaoproblema import Visaoproblema

class JanelaRegistroPaciente(JanelaPadrao):
    def __init__(self, master, cpf,  visao: Visaopaciente, controle: ControlePaciente,
                 controlemedico: ControleProfissionalSaude, visaoproblema: Visaoproblema,
                 controleproblema: ControleProblema):

        super().__init__(master)
        self.master = master
        self.cpf_valor = cpf
        self.visaopaciente = visao
        self.controlepaciente = controle
        self.controlemedico = controlemedico
        self.controleproblema = controleproblema
        self.visaoproblema = visaoproblema

        # TODO: deixar bonitinho o título(colocar logo)
        self.master.title("Cadastro Paciente")

        self.var = StringVar()
        self.holder_list = []

        self.configurarJanelaRegistro()

    def configurarJanelaRegistro(self):

        # IMAGEM DE FUNDO DA TELA
        bg_panel = Image.open('assets/sarah_registro.png')
        bg_panel_photo = ImageTk.PhotoImage(bg_panel)
        bg_panel = Label(self.master, image=bg_panel_photo)
        bg_panel.image = bg_panel_photo
        bg_panel.pack(fill='both')
        self.camposPaciente()

    def camposPaciente(self):

        # CRIANDO O FRAME ONDE AS CAIXINHAS DE NOME, IDADE, ETC... IRÃO FICAR
        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.7, anchor=CENTER, relwidth=0.35, relheight=0.55)
        #
        # # CRIANDO ATRIBUTOS COMO INSTÂNCIA DA CLASSE SÓ PARA SEREM ACESSÍVEIS NA FUNÇÃO
        # # 'REGISTRAR'
        #
        # # TODO: Passar os atributos para controle
        #
        self.sexo_var = StringVar()
        self.sexo_combobox = ttk.Combobox(label, textvariable=self.sexo_var, width=17)
        self.sexo_combobox['values'] = ('Feminino', 'Masculino', 'Outros')
        self.sexo_combobox.current()

        label_nome = tkinter.Label(label, text='Nome:', font=self.fonte)
        label_nome.place(x=20, y=20)
        self.entry_nome = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_nome.place(x=120, y=20)

        label_idade = tkinter.Label(label, text='Idade:', font=self.fonte)
        label_idade.place(x=20, y=60)
        self.entry_idade = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_idade.place(x=120, y=60)

        label_sexo = tkinter.Label(label, text='Sexo:', font=self.fonte)
        label_sexo.place(x=20, y=100)
        self.sexo_combobox.place(x=120, y=100)

        label_cpf = tkinter.Label(label, text='CPF:', font=self.fonte)
        label_cpf.place(x=20, y=140)
        self.entry_cpf = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_cpf.place(x=120, y=140)

        label_localidade = tkinter.Label(label, text='Localidade:', font=self.fonte)
        label_localidade.place(x=20, y=180)
        self.entry_localidade = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_localidade.place(x=120, y=180)

        label_senha = tkinter.Label(label, text='Senha:', font=self.fonte)
        label_senha.place(x=20, y=220)
        self.entry_senha = tkinter.Entry(label, show='*', font=self.fonte_menor)
        self.entry_senha.place(x=120, y=220)

        label_sintomas = tkinter.Label(label, text='Sintomas:', font=self.fonte)
        label_sintomas.place(x=20, y=260)
        self.entry_sintomas = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_sintomas.place(x=120, y=260)

        botao_registrar = tkinter.Button(self.master, text='Registrar', font=self.fonte_menor, command=self.Registrar)
        botao_registrar.place(relx=0.8, rely=0.95, anchor=CENTER, width=100, height=30)

    def Registrar(self):

        # ARMAZENANDO OS VALORES INSERIDOS PRA VER SE TAVA DANDO CERTO (ESTÁ) :D
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        cpf = self.entry_cpf.get()
        self.cpf_valor = cpf
        sexo = self.sexo_combobox.get()
        localidade = self.entry_localidade.get()
        senha = self.entry_senha.get()
        sintomas = self.entry_sintomas.get()

        # VERIFICAR SE AS INFORMAÇÕES SÃO VÁLIDAS, CASO NÃO CHAMA A JANELA SECUNDÁRIA
        if not nome or not idade or not sexo or not cpf or not localidade:
            button_open = tkinter.Button(
                self.master,
                text="Informações invalidas",
                command=self.JanelaSecundaria
            )
        else:
            self.visaopaciente.inserir(nome, idade, cpf, sexo, localidade, senha)
            self.visaoproblema.inserir(self.cpf_valor, sintomas)
            self.configurarJanelaHome()
            # self.configurarJanelaLogin()

    # FUNÇÃO QUE CONFIGURA JANELA SECUNDÁRIA CASO AS INFORMAÇÕES SEJAM INVÁLIDAS
    def JanelaSecundaria(self):
        JanelaErro(self.master)

    # FUNÇÃO RESPONSÁVEL POR CHAMAR A JANELA HOME
    def configurarJanelaHome(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaHomePaciente(
            master=self.master,
            cpf=self.cpf_valor,
            visao=self.visaopaciente,
            visaoproblema=self.visaoproblema,
            controlePaciente=self.controlepaciente,
            controlemedico=self.controlemedico,
            controleproblema=self.controleproblema
        )
