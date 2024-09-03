from controle.ControlePaciente import ControlePaciente
from controle.ControleProblema import ControleProblema
from persistencia.PersistenciaPaciente import PersistenciaPaciente
from persistencia.PersistenciaProblema import PersistenciaProblema
from visao.JanelaLogin import JanelaLogin
from tkinter import *
from controle.ControleConsulta import ControleConsulta
from persistencia.PersistenciaConsulta import PersistenciaConsulta

from visao.visaopaciente import Visaopaciente
from visao.visaoproblema import Visaoproblema
from visao.visaoprofissional import Visaoprofissional
from controle.ControleProfissionalSaude import ControleProfissionalSaude

from persistencia.PersistenciaProfissionalSaude import PersistenciaProfissionalSaude

master = Tk()

persistenciaProfissionalSaude = PersistenciaProfissionalSaude('profissionais.db')
persistenciaPaciente = PersistenciaPaciente('pacientes.db')
controleProfissionalSaude = ControleProfissionalSaude(persistenciaProfissionalSaude)
controlePaciente = ControlePaciente(persistenciaPaciente)
visaoProfissionalSaude = Visaoprofissional(controleProfissionalSaude)
visaoPaciente = Visaopaciente(controlePaciente)

persistenciaProblema = PersistenciaProblema('problemas.db')
controleProblema = ControleProblema(persistenciaProblema)
visaoProblema = Visaoproblema(controleProblema)

persistenciaConsulta = PersistenciaConsulta('consulta.db', persistenciaPaciente, persistenciaProfissionalSaude)
controleConsulta = ControleConsulta(persistenciaConsulta)

jan = JanelaLogin(
    master=master,
    visaopaciente=visaoPaciente,
    controlepaciente=controlePaciente,
    visaomedico=visaoProfissionalSaude,
    controlemedico=controleProfissionalSaude,
    controleConsulta=controleConsulta,
    visaoproblema=visaoProblema,
    controleproblema=controleProblema
)

master.mainloop()
for i in persistenciaProfissionalSaude.carregar_profissionais():
    print(i)
for i in persistenciaPaciente.carregar_pacientes():
    print(i)
