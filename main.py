from visao.VisaoLogin import JanelaLogin
from tkinter import *
from visao.VisaoProfissional import VisaoProfissionalSaude
from controle.ControleProfissionalSaude import ControleProfissionalSaude
from persistencia.PersistenciaProfissionalSaude import PersistenciaProfissionalSaude

master = Tk()

pps = PersistenciaProfissionalSaude('profissionais.db')
cps = ControleProfissionalSaude(pps)
vps = VisaoProfissionalSaude(cps)

jan = JanelaLogin(master, vps, 0)
master.mainloop()
for i in pps.carregar_profissionais():
    print(i)
