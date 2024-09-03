import tkinter as tk
from tkinter import ttk, messagebox
from controle.ControleAgendamento import ControleAgendamento
from modelo.Paciente import Paciente
from modelo.ProfissionalSaude import ProfissionalSaude
from modelo.Consulta import Consulta
from datetime import datetime

class JanelaAgendamento(tk.Toplevel):
    def __init__(self, master, medico: ProfissionalSaude, paciente: Paciente, 
                 controleagendamento: ControleAgendamento):
        super().__init__(master)
        self.title("Sistema de Agendamento")
        self.geometry("500x400")

        self.medico = medico
        self.paciente = paciente
        self.controlegendamento = controleagendamento
        
        

        # Título
        tk.Label(self, text="Sistema de Agendamento", font=("Arial", 16)).pack(pady=10)

        # Listbox para mostrar os agendamentos
        self.listbox_agendamentos = tk.Listbox(self, height=15, width=70)
        self.listbox_agendamentos.pack(pady=10)

        # Botões para ações
        self.btn_ver = tk.Button(self, text="Ver Detalhes", command=self.ver_detalhes)
        self.btn_ver.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_editar = tk.Button(self, text="Editar", command=self.editar_agendamento)
        self.btn_editar.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_excluir = tk.Button(self, text="Excluir", command=self.excluir_agendamento)
        self.btn_excluir.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_novo = tk.Button(self, text="Novo Agendamento", command=self.novo_agendamento)
        self.btn_novo.pack(side=tk.RIGHT, padx=5, pady=5)

        # Carregar agendamentos
        self.carregar_agendamentos()

    def carregar_agendamentos(self):
        self.listbox_agendamentos.delete(0, tk.END)
        agendamentos = self.controle_agendamento.carregar_todos_agendamentos()
        for agendamento in agendamentos:
            display_text = f"Paciente ID: {agendamento.paciente.id} | Profissional ID: {agendamento.profissional.id} | Data/Horário: {agendamento.data_horario}"
            self.listbox_agendamentos.insert(tk.END, display_text)

    def ver_detalhes(self):
        selecionado = self.listbox_agendamentos.curselection()
        if selecionado:
            agendamento = self.listbox_agendamentos.get(selecionado)
            messagebox.showinfo("Detalhes do Agendamento", agendamento)
        else:
            messagebox.showwarning("Seleção Necessária", "Por favor, selecione um agendamento.")

    def editar_agendamento(self):
        selecionado = self.listbox_agendamentos.curselection()
        if selecionado:
            agendamento = self.listbox_agendamentos.get(selecionado)
            # Aqui você pode abrir outra janela para editar o agendamento
            messagebox.showinfo("Editar Agendamento", "Função de edição não implementada ainda.")
        else:
            messagebox.showwarning("Seleção Necessária", "Por favor, selecione um agendamento.")

    def excluir_agendamento(self):
        selecionado = self.listbox_agendamentos.curselection()
        if selecionado:
            agendamento = self.listbox_agendamentos.get(selecionado)
            confirm = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o agendamento?\n\n{agendamento}")
            if confirm:
                # Excluir o agendamento
                self.controlegendamento.excluir_agendamento(agendamento)  # Assumindo que você tem esse método
                self.carregar_agendamentos()
        else:
            messagebox.showwarning("Seleção Necessária", "Por favor, selecione um agendamento.")

    def novo_agendamento(self):
        # Abre uma nova janela para inserir a data e hora do novo agendamento
        nova_janela = tk.Toplevel(self)
        nova_janela.title("Novo Agendamento")
        nova_janela.geometry("300x200")

        tk.Label(nova_janela, text="Data (dd/mm/yyyy):").pack(pady=10)
        data_var = tk.StringVar()
        data_entry = tk.Entry(nova_janela, textvariable=data_var)
        data_entry.pack(pady=5)

        tk.Label(nova_janela, text="Hora (HH:MM):").pack(pady=10)
        hora_var = tk.StringVar()
        hora_entry = tk.Entry(nova_janela, textvariable=hora_var)
        hora_entry.pack(pady=5)

        def confirmar_agendamento():
            data = data_var.get()
            hora = hora_var.get()
            print(self.medico)
            if self.paciente and self.medico:
                consulta = Consulta(0,profissional=self.medico, paciente=self.paciente, valor= self.medico.precoConsulta, data_horario=data)
            if not data or not hora:
                messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            else:
                try:
                    # Verifica se a data e hora são válidas
                    data_hora = datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")

                    # Cria um novo agendamento e salva no banco de dados
                    # novo_agendamento = self.controleagendamento.inserir(
                    
                    # )
                    # if novo_agendamento:
                    #     messagebox.showinfo("Sucesso", f"Novo agendamento criado para {data_hora}.")
                    #     nova_janela.destroy()
                    #     self.carregar_agendamentos()  # Recarrega os agendamentos na lista
                    # else:
                    #     messagebox.showerror("Erro", "Erro ao salvar o agendamento.")

                except ValueError:
                    messagebox.showerror("Erro", "Data ou hora inválida.")

        btn_confirmar = tk.Button(nova_janela, text="Confirmar", command=confirmar_agendamento)
        btn_confirmar.pack(pady=10)
