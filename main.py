from controle.ControlePaciente import ControlePaciente
from persistencia.PersistenciaPaciente import PersistenciaPaciente
from visao.JanelaLogin import JanelaLogin
from tkinter import *

from visao.visaopaciente import Visaopaciente
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

jan = JanelaLogin(master, vp, vps, cp, pp, cps, pps)
master.mainloop()
for i in pps.carregar_profissionais():
    print(i)
for i in pp.carregar_pacientes():
    print(i)
