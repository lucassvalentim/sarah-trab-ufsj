from controle.ControlePaciente import ControlePaciente
from controle.ControleProblema import ControleProblema
from persistencia.PersistenciaPaciente import PersistenciaPaciente
from persistencia.PersistenciaProblema import PersistenciaProblema
from visao.JanelaLogin import JanelaLogin
from tkinter import *

from visao.visaopaciente import Visaopaciente
from visao.visaoproblema import Visaoproblema
from visao.visaoprofissional import Visaoprofissional
from controle.ControleProfissionalSaude import ControleProfissionalSaude

from persistencia.PersistenciaProfissionalSaude import PersistenciaProfissionalSaude

master = Tk()

pps = PersistenciaProfissionalSaude('profissionais.db')
pp = PersistenciaPaciente('pacientes.db')
cps = ControleProfissionalSaude(pps)
cp = ControlePaciente(pp)
vps = Visaoprofissional(cps)
vp = Visaopaciente(cp)

prob = PersistenciaProblema('problemas.db')
cprob = ControleProblema(prob)
vprob = Visaoproblema(cprob)

jan = JanelaLogin(master, vp, vps, cp, pp, cps, pps, prob, cprob, vprob)
master.mainloop()
for i in pps.carregar_profissionais():
    print(i)
for i in pp.carregar_pacientes():
    print(i)
