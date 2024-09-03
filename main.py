from controle.ControlePaciente import ControlePaciente
from controle.ControleProblema import ControleProblema
from persistencia.PacienteDAO import PacienteDAO
from persistencia.ProblemaDAO import ProblemaDAO
from visao.JanelaLogin import JanelaLogin
from tkinter import *
from controle.ControleConsulta import ControleConsulta
from persistencia.ConsultaDAO import ConsultaDAO

from visao.visaopaciente import Visaopaciente
from visao.visaoproblema import Visaoproblema
from visao.visaoprofissional import Visaoprofissional
from controle.ControleProfissionalSaude import ControleProfissionalSaude

from persistencia.ProfissionalSaudeDAO import ProfissionalSaudeDAO

master = Tk()

persistenciaProfissionalSaude = ProfissionalSaudeDAO('profissionais.db')
persistenciaPaciente = PacienteDAO('pacientes.db')
controleProfissionalSaude = ControleProfissionalSaude(persistenciaProfissionalSaude)
controlePaciente = ControlePaciente(persistenciaPaciente)
visaoProfissionalSaude = Visaoprofissional(controleProfissionalSaude)
visaoPaciente = Visaopaciente(controlePaciente)

persistenciaProblema = ProblemaDAO('problemas.db')
controleProblema = ControleProblema(persistenciaProblema)
visaoProblema = Visaoproblema(controleProblema)

persistenciaConsulta = ConsultaDAO('consulta.db', persistenciaPaciente, persistenciaProfissionalSaude)
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
