import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from gui.JanelaHome import JanelaHome
from gui.JanelaPadrao import JanelaPadrao
from gui.JanelaErro import JanelaErro

class JanelaRegistro(JanelaPadrao):
    def __init__(self, master, tipo):
        super().__init__(master)
        self.master = master
        # TODO: deixar bonitinho o título(colocar logo)
        self.master.title("Cadastro")

        self.var = StringVar()
        self.tipo = tipo
        self.holder_list = []

        self.configurarJanelaRegistro()

    def configurarJanelaRegistro(self):

        # IMAGEM DE FUNDO DA TELA
        bg_panel = Image.open('/home/izzy/sarah-trab-ufsj/assets/sarah_registro.png')
        bg_panel_photo = ImageTk.PhotoImage(bg_panel)
        bg_panel = Label(self.master, image=bg_panel_photo)
        bg_panel.image = bg_panel_photo
        bg_panel.pack(fill='both')

        # CRIANDO FRAME ONDE VAI FICAR AS CAIXINHAS DE PACIENTE E MÉDICO
        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # CRIANDO BOTÃO PACIENTE
        paciente = Radiobutton(label, text="Paciente", variable=self.var, value='Paciente',
                               command=self.purchase)
        paciente.config(indicatoron=0, width=12, value='Paciente')
        paciente.grid(row=0, column=0)

        # ADICIONANDO O BOTÃO NA HOLDER_LIST --> ISSO SERVE PRA PODER APAGAR ELES DPS NA FUNÇÃO
        # PURCHASE
        self.holder_list.append(paciente)

        # CRIANDO BOTÃO MÉDICO
        medico = Radiobutton(label, text="Medico", variable=self.var, value='Medico',
                             command=self.camposProfissional)
        medico.config(indicatoron=0, width=12, value='Medico')
        medico.grid(row=0, column=1)
        # ADICIONANDO O BOTÃO NA HOLDER_LIST --> ISSO SERVE PRA PODER APAGAR ELES DPS NA FUNÇÃO
        # PURCHASE
        self.holder_list.append(medico)

    # FUNÇÃO RESPONSÁVEL POR DELETAR AS CAIXINHAS DE ESCOLHA PACIENTE E MÉDICO :D
    def purchase(self):

        # TO FAZENDO ISSO SO PRA PRINTAR OS VALORES DA LISTA PRA VER SE TAVA DANDO
        # CERTO
        print(self.holder_list)
        selected_value = self.var.get()
        # VERIFICANDO SE É PACIENTE, SE FOR CHAMA A FUNÇÃO CAMPOSPACIENTE()
        if selected_value == 'Paciente':
            print(selected_value)
            for widget in self.holder_list:
                widget.grid_remove()

            self.holder_list = []
            self.master.update_idletasks()
            self.camposPaciente()

        # VERIFICANDO SE É MÉDICO, SE FOR CHAMA A FUNÇÃO CAMPOSPROFISSIONAL()
        elif selected_value == 'Medico':
            print(selected_value)
            for widget in self.holder_list:
                widget.grid_remove()

            self.holder_list = []
            self.master.update_idletasks()
            self.camposProfissional()

    def camposPaciente(self):

        # DEFININDO QUE O TIPO É PACIENTE
        self.tipo = 1

        # CRIANDO O FRAME ONDE AS CAIXINHAS DE NOME, IDADE, ETC... IRÃO FICAR
        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.7, anchor=CENTER, relwidth=0.35, relheight=0.55)

        # CRIANDO ATRIBUTOS COMO INSTÂNCIA DA CLASSE SÓ PARA SEREM ACESSÍVEIS NA FUNÇÃO
        # 'REGISTRAR'

        # TODO: Passar os atributos para controle

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

        botao_registrar = tkinter.Button(self.master, text='Registrar', font=self.fonte_menor, command=self.Registrar)
        botao_registrar.place(relx=0.8, rely=0.95, anchor=CENTER, width=100, height=30)

    def camposProfissional(self):

        # DEFININDO QUE O TIPO É MEDICO
        self.tipo = 2

        # CRIANDO O FRAME ONDE AS CAIXINHAS DE NOME, IDADE, ETC... IRÃO FICAR
        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.7, anchor=CENTER, relwidth=0.65, relheight=0.55)

        # CRIANDO ATRIBUTOS COMO INSTÂNCIA DA CLASSE SÓ PARA SEREM ACESSÍVEIS NA FUNÇÃO
        # 'REGISTRAR'

        # TODO: Passar os atributos para controle
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

        label_especialiacao = tkinter.Label(label, text='Especialização:', font=self.fonte)
        label_especialiacao.place(x=300, y=20)
        self.entry_especializacao = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_especializacao.place(x=450, y=20)

        label_crm = tkinter.Label(label, text='CRM:', font=self.fonte)
        label_crm.place(x=300, y=60)
        self.entry_crm = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_crm.place(x=450, y=60)

        label_formacao = tkinter.Label(label, text='Formação:', font=self.fonte)
        label_formacao.place(x=300, y=100)
        self.entry_formacao = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_formacao.place(x=450, y=100)

        label_tempo_ativ = tkinter.Label(label, text='Tempo Atividade:', font=self.fonte)
        label_tempo_ativ.place(x=300, y=140)
        self.entry_tempo_ativ = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_tempo_ativ.place(x=450, y=140)

        label_convenios = tkinter.Label(label, text='Convênios:', font=self.fonte)
        label_convenios.place(x=300, y=180)
        self.entry_convenios = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_convenios.place(x=450, y=180)

        label_preco_consulta = tkinter.Label(label, text='Valor da consulta:', font=self.fonte)
        label_preco_consulta.place(x=300, y=220)
        self.entry_preco_consulta = tkinter.Entry(label, font=self.fonte_menor)
        self.entry_preco_consulta.place(x=450, y=220)

        botao_registrar = tkinter.Button(self.master, text='Registrar', font=self.fonte_menor, command=self.Registrar)
        botao_registrar.place(relx=0.90, rely=0.95, anchor=CENTER, width=100, height=30)

    def Registrar(self):

        # ARMAZENANDO OS VALORES INSERIDOS PRA VER SE TAVA DANDO CERTO (ESTÁ) :D
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        sexo = self.sexo_combobox.get()
        cpf = self.entry_cpf.get()
        localidade = self.entry_localidade.get()
        senha = self.entry_senha.get()

        # VERIFICAR SE AS INFORMAÇÕES SÃO VÁLIDAS, CASO NÃO CHAMA A JANELA SECUNDÁRIA
        if not nome or not idade or not sexo or not cpf or not localidade or not senha:
            button_open = tkinter.Button(
                self.master,
                text="Informações invalidas",
                command=self.JanelaSecundaria()
            )
        else:
            print("Nome:", nome)
            print("Idade:", idade)
            print("Sexo:", sexo)
            print("CPF:", cpf)
            print("Localidade:", localidade)
            print("Senha:", senha)
            self.configurarJanelaHome()

    # FUNÇÃO QUE CONFIGURA JANELA SECUNDÁRIA CASO AS INFORMAÇÕES SEJAM INVÁLIDAS
    def JanelaSecundaria(self):
        JanelaErro(self.master)

    # FUNÇÃO RESPONSÁVEL POR CHAMAR A JANELA HOME
    def configurarJanelaHome(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        JanelaHome(self.master, self.tipo)
