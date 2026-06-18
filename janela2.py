from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
class Janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha janela")
        
        # Largura , altura e posição da janela.
        self.setGeometry(10,20,800,400)
        self.texto =  QLabel("Clique no botão abaixo")
        self.botao1 =  QPushButton("OK")
        self.botao2 =  QPushButton("Cancelar")
        
        # para organizar os controles(label, pushbutton) usaremos o comando
        # QVBoxLayout, para distribuir os controles de forma vertical na tela.
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.texto)
        layout_vertical.addWidget(self.botao1)
        layout_vertical.addWidget(self.botao2)

        # Adicionar o layout vertical a tela
        self.setLayout(layout_vertical)



app = QApplication(sys.argv)
tela = Janela2()
tela.show()
app.exec()