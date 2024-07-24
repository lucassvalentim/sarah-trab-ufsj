from modelo.Paciente import Paciente
from modelo.ProfissionalSaude import ProfissionalSaude
from gui.JanelaCadastro import JanelaCadastro
from tkinter import *
from tkinter import messagebox

# paciente = Paciente(0, "Lucas", 21, "703223212311", "Masculino", "sjdr")
# profissionaSaude = ProfissionalSaude(0, "Igor", 28, "123123123", "Masculino",
#                                      "sjdr", "Ortopedista", "210391-23",
#                                      "Medico", "4 anos", "Unimed", 230.00)
#
# paciente.exibirDados()
# profissionaSaude.exibirDados()

master = Tk()
jan = JanelaCadastro(master)
master.mainloop()

