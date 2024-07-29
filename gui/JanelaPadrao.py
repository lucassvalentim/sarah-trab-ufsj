
class JanelaPadrao:
    def __init__(self, master=None):
        self.master = master
        # INICIALIZA AS CARACTERÍSITCAS DA TELA DO PROGRAMA
        # TODO: arrumar a foto nas janelas (ñ ta aparecendo a flor) :(
        self.master.geometry('960x540')
        self.master.resizable(0, 0)
        self.selectionbar_color = '#eff5f6'
        self.sidebar_color = '#CFCFCF'
        self.img_color = '#FCFCFC'
        self.fonte = ('Arial', 14)
        self.fonte_menor = ('Arial', 10)