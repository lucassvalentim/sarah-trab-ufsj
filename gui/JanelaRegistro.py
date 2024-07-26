import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from gui.JanelaPadrao import JanelaPadrao

class JanelaRegistro(JanelaPadrao):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Cadastro")
        self.master.geometry('960x540')
        self.master.resizable(0, 0)
        self.master.var = IntVar()
        self.master.holder_list = []
        self.configurarJanelaRegistro()

    def configurarJanelaRegistro(self):

        self.master.bg_panel = Image.open('/home/izzy/Documentos/ATT-gui/sarah-trab-ufsj/gui/sarah_registro.png')
        photo = ImageTk.PhotoImage(self.master.bg_panel)
        self.master.bg_panel = Label(self.master, image=photo)
        self.master.bg_panel.image = photo
        self.master.bg_panel.pack(fill='both', expand='yes')

        fonte = ('Arial', 14)
        fonte_menor = ('Arial', 12)

        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # TODO: add logica para excluir os botoes e chamar as funcoes
        var = IntVar()
        paciente = Radiobutton(label, text="Paciente", variable=var, value=1, command=self.purchase)
        paciente.config(indicatoron=0, width=12, value='Paciente')
        paciente.grid(row=0, column=0)
        self.master.holder_list.append(paciente)

        medico = Radiobutton(label, text="Medico", variable=var, value=2, command=self.camposProfissional)
        medico.config(indicatoron=0, width=12, value='Medico')
        medico.grid(row=0, column=1)

        # medico.pack(anchor=NE)
        # self.master.attributes("-alpha", 0.9)
        # rightFrame = Frame(self.master, width=670, height=620, bg="#8B0000", relief="raise")
        # rightFrame.pack(side=RIGHT)
        # letFrame = Frame(self.master, width=400, height=620, bg="#8B0000", relief="raise")
        #
        # tipoLabel = Label(rightFrame, text="Tipo de Usuário", bg="#8B0000", font=("Arial", 30, "bold"), fg="White")
        # tipoLabel.place(x=200, y=50)
        #
        # #titulo da pagina da esquerda
        # titleLabel = Label(letFrame, text="SARAH", bg="#8B0000", font=("Georgia", 50, "bold"), fg="White")
        #
        # #colocando os elementos na tela da esquerda
        # letFrame.pack(side=LEFT)
        # titleLabel.place(x=60, y=250)
        # rightFrame.pack(side=RIGHT)
        #
        # self.tipoUsuario = StringVar()
        # self.tipoUsuario.set("Paciente")
        #
        # tipoPaciente = ttk.Radiobutton(rightFrame, text="Paciente", variable=self.tipoUsuario, value="Paciente", command=self.mostrarCampos)
        # tipoPaciente.place(x=200, y=120)
        #
        # tipoProfissional = ttk.Radiobutton(rightFrame, text="Profissional de Saúde", variable=self.tipoUsuario, value="Profissional", command=self.mostrarCampos)
        # tipoProfissional.place(x=200, y=150)
        #
        # self.camposFrame = Frame(rightFrame, bg="#8B0000")
        # self.camposFrame.place(x=50, y=200)
        #
        # concluirButton = ttk.Button(rightFrame, text="Concluir Registro", width=20)
        # concluirButton.place(x=200, y=590)
        #
        # self.mostrarCampos()



    # def mostrarCampos(self):
    #     for widget in self.camposFrame.winfo_children():
    #         widget.destroy()
    #
    #     if self.tipoUsuario.get() == "Paciente":
    #         self.camposPaciente()
    #     else:
    #         self.camposProfissional()

    def purchase(self):
        print(self.master.holder_list)
        for widget in self.master.holder_list:
            widget.grid_forget()

    def camposPaciente(self):

        fonte = ('Arial', 14)
        fonte_menor = ('Arial', 12)

        label = tkinter.Frame(self.master, relief=FLAT)
        label.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        label_nome = tkinter.Label(label, text='Nome', font=fonte, padx=5, pady=5)
        label_nome.pack()
        entry_nome = tkinter.Entry(label, font=fonte_menor)
        entry_nome.pack()
        # Label(self.camposFrame, text="Nome", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        # Entry(self.camposFrame, width=40).grid(row=0, column=1, padx=10, pady=10)
        #
        # Label(self.camposFrame, text="Idade", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        # Entry(self.camposFrame, width=40).grid(row=1, column=1, padx=10, pady=10)
        #
        # Label(self.camposFrame, text="CPF", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        # Entry(self.camposFrame, width=40).grid(row=2, column=1, padx=10, pady=10)
        #
        # Label(self.camposFrame, text="Sexo", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        # Entry(self.camposFrame, width=40).grid(row=3, column=1, padx=10, pady=10)
        #
        # Label(self.camposFrame, text="Localidade", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        # Entry(self.camposFrame, width=40).grid(row=4, column=1, padx=10, pady=10)

    def camposProfissional(self):
        tam = 6
        Label(self.camposFrame, text="Nome", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=0, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=0, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Idade", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=1, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=1, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="CPF", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=2, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=2, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Sexo", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=3, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=3, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Localidade", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=4, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=4, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Especialização", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=5, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=5, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="CRM", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=6, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=6, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Formação", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=7, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=7, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Tempo de Atividade", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=8, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=8, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Convênios", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=9, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=9, column=1, padx=10, pady=tam)

        Label(self.camposFrame, text="Preço da Consulta", bg="#8B0000", font=("Arial", 11), fg="White").grid(row=10, column=0, padx=10, pady=tam, sticky=W)
        Entry(self.camposFrame, width=40).grid(row=10, column=1, padx=10, pady=tam)
