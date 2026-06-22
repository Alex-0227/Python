# ================================================================= CRIAÇÃO JANELA ================================================================================================
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTableWidget, QVBoxLayout, QHBoxLayout,QTableWidgetItem, QPushButton
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.QtCore import Qt
from sys import argv
import webbrowser 


class Caixa(QWidget):
    
    

    def __init__(self):

        self.linha = 0    
        self.valor_total = 0.0

        super().__init__()
        self.setWindowTitle("Pagina Python")
        self.setGeometry(150,50,1600,900)

        self.setWindowIcon(QIcon("icons8.png"))

        # =============================================================== CRIAÇÃO LAYOUTS ======================================================================================
        # Criar o layout horizontal ---------------------------------------------------------------------------------------
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.setSpacing(0)
        self.layout_horizontal.setContentsMargins(0,0,0,0)


        # Vamos criar as duas colunas: Esquerda e Direita
        # e alterar as cores de fundo de cada uma:

        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#E5F0FE}")
        self.label_col_direita.setFixedWidth(800)

        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#E5F0FE}")
        self.label_col_esquerda.setFixedWidth(800)

        # ========================================================== COLUNA ESQUERDA ========================================================================================
        # Criar o layout dos elementos da coluna da esquerda. Este layout é vertical --------------------------------------------------------------------------------------
        self.layout_vert_col_esq = QVBoxLayout()

        # vamos criar uma label para adicionar o logo 
        self.label_logo = QLabel()
        # Vamos setar o Pixmap à label para carregar a imagem
        self.label_logo.setPixmap(QPixmap("dogo.jpg"))
        # Ajustar a imagem à label
        self.label_logo.setScaledContents(True)



        # Adicionando os elementos á coluna da esquerda --------------------------------------------------------------------------------------------------------
        # Adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)

        # Setar o layout vertical à label coluna esquerda
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)
        
        # ================================================================ FIM COLUNA ESQUERDA ===============================================================================


        # ========================================================== COLUNA DIREITA ========================================================================================
        # Criar o layout dos elementos da coluna da esquerda. Este layout é vertical --------------------------------------------------------------------------------------
        self.layout_vert_col_dir = QVBoxLayout()

        # criar a label do codigo do produto ----------------------------------------------------------------------------------
        self.label_cod_titulo = QLabel("Ajude um amiguinho a \n" \
        "encontrar um novo lar\n" \
        "Seja voluntário!")
        self.label_cod_titulo.setStyleSheet("QLabel {font-weight:bold; font-size:30pt; color:#000000}")

        # NOME COMPLETO ================================================ 
        self.label_inserir_nome = QLabel("Nome Completo")
        self.label_inserir_nome.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#000000}")        
        self.edit_inserir_nome = QLineEdit()
        self.edit_inserir_nome.setStyleSheet("QLineEdit{font-size:15pt;background-color:#ABB8CF;}")
        self.edit_inserir_nome.setFixedHeight(40)

        # E-MAIL =======================================================
        self.label_inserir_email = QLabel("E-Mail")
        self.label_inserir_email.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#000000}")         
        self.edit_inserir_email = QLineEdit()
        self.edit_inserir_email.setStyleSheet("QLineEdit{font-size:15pt;background-color:#ABB8CF;}")
        self.edit_inserir_email.setFixedHeight(40)
        # SENHA ========================================================
        self.label_inserir_senha = QLabel("Senha")
        self.label_inserir_senha.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#000000}")                 
        self.edit_inserir_senha = QLineEdit()
        self.edit_inserir_senha.setStyleSheet("QLineEdit{font-size:15pt;background-color:#ABB8CF;}")
        self.edit_inserir_senha.setFixedHeight(40)


        self.label_fazer_login =  QLabel("Fazer login com...")
        self.label_fazer_login.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#000000}")

        self.botao1 = QPushButton("")
        self.botao1.clicked.connect(
            lambda:webbrowser.open("https://www.google.com")    
        )
        self.botao1.setStyleSheet("QPushButton{border-radius:10px;font-size:10pt;background-color:#ABB8CF;color:#000000} QPushButton:hover {background-color:#4C525C; color: white;}")
        self.botao1.setIcon(QIcon("icons8G.png")) 
        self.botao1.setFixedHeight(40)
       #self.botao1.setStyleSheet("QPushButton {font-weight:bold; font-size:20pt;background-color:#C56AE6; color:#000000}") 
       
                              
        self.botao2 = QPushButton("")
        self.botao2 = QPushButton("")
        self.botao2.clicked.connect(
            lambda:webbrowser.open("https://www.discord.com"))   
        self.botao2.setIcon(QIcon("icons8D.png"))  
        self.botao2.setFixedHeight(40)           
        self.botao2.setStyleSheet("QPushButton{font-weight:bold; border-radius:10px;font-size:20pt;background-color:#ABB8CF;color:#000000} QPushButton:hover {background-color:#4C525C; color: white;}")   

        # Adicionar o codigo
        
        self.layout_vert_col_dir.addWidget(self.label_cod_titulo)

        self.layout_vert_col_dir.addWidget(self.label_inserir_nome)
        self.layout_vert_col_dir.addWidget(self.edit_inserir_nome)

        self.layout_vert_col_dir.addWidget(self.label_inserir_email)
        self.layout_vert_col_dir.addWidget(self.edit_inserir_email)

        self.layout_vert_col_dir.addWidget(self.label_inserir_senha)
        self.layout_vert_col_dir.addWidget(self.edit_inserir_senha)

        self.layout_vert_col_dir.addWidget(self.label_fazer_login)
        self.layout_vert_col_dir.addWidget(self.botao1)
        self.layout_vert_col_dir.addWidget(self.botao2)
















        # Setar o layout vertical à label coluna direita
        self.label_col_direita.setLayout(self.layout_vert_col_dir)

        # ================================================================== ADICIONAR OS LAYOUTS NA JANELA ==============================================================
        # Adicionar as colunas da esquerda e direita ao layout horizontal
        # lembrar que essa parte tem que sempre ficar depois de ter alterado todos
        # os detalhes doque irá ficar dentro
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)
        # Setar o layout horizontal à nossa janela
        self.setLayout(self.layout_horizontal)


        
app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()