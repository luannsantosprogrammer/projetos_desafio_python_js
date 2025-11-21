from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys




class Navegador(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Auxiliar")




        self.linha_navegacao = QHBoxLayout()
        self.bt_ir = QPushButton("▶️")
        self.bt_voltar = QPushButton("◀️")
        self.bt_recarregar = QPushButton("🔄")
        self.barra_pesquisa = QLineEdit()
        self.bt_nova_aba = QPushButton("Nova aba")


        self.bt_voltar.clicked.connect(self.voltar)
        self.bt_ir.clicked.connect(self.ir)
        self.bt_recarregar.clicked.connect(self.recarregar)
        self.bt_nova_aba.clicked.connect(self.criar_nova_aba)
        self.barra_pesquisa.returnPressed.connect(self.navegando)

        self.linha_navegacao.addWidget(self.bt_voltar)
        self.linha_navegacao.addWidget(self.bt_ir)
        self.linha_navegacao.addWidget(self.bt_recarregar)
        self.linha_navegacao.addWidget(self.barra_pesquisa)
        self.linha_navegacao.addWidget(self.bt_nova_aba)

        lista = ['Selecione automação','Automação 1','Automação 2']

        self.linha_automacoes = QHBoxLayout()
        self.selecionador = QComboBox()
        self.selecionador.addItems(lista)
        self.selecionador.currentIndexChanged.connect(self.selecionado_automacao)

        self.linha_automacoes.addWidget(self.selecionador)

        self.abas = QTabWidget()
        self.abas.setTabsClosable(True)
        self.abas.tabCloseRequested.connect(self.fechar_aba)

        self.organizado_vertical = QVBoxLayout()
        self.organizado_vertical.addLayout(self.linha_navegacao)     
        self.organizado_vertical.addLayout(self.linha_automacoes)
        self.organizado_vertical.addWidget(self.abas)     


        self.wid = QWidget()
        self.wid.setLayout(self.organizado_vertical)
        self.setCentralWidget(self.wid) 

        self.criar_nova_navegacao("http://www.google.com")
        self.barra_pesquisa.setText("http://www.google.com")

    def voltar(self):
        aba_atual = self.abas.currentWidget()
        if aba_atual:
            aba_atual.back()

    def ir(self):
        aba_atual = self.abas.currentWidget()
        if aba_atual:
            aba_atual.forward()
    def recarregar(self):
        aba_atual = self.abas.currentWidget()
        if aba_atual:
            aba_atual.reload()

    def criar_nova_navegacao(self,url):
        nova_aba = QWebEngineView()
        nova_aba.setUrl(QUrl(url))
        index = self.abas.addTab(nova_aba, "Nova Página")
        self.abas.setCurrentIndex(index)

    def criar_nova_aba(self):
        self.criar_nova_navegacao("http://www.google.com")

    def fechar_aba(self,index):
        self.abas.removeTab(index)
        
    def navegando(self):
        aba_atual = self.abas.currentWidget()
        link = self.barra_pesquisa.text()
        if not link.startswith("http"):
            link = "https://"+link

        aba_atual.setUrl(QUrl(link))

    def selecionado_automacao(self):
        print(self.selecionador.currentText())

app = QApplication(sys.argv)
nav = Navegador()
nav.show()
sys.exit(app.exec_())