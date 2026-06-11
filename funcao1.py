# Vamos importar a biblioteca de módulos OS(operation system)
# para usar uma função chamada system e, executar o comando
# clear(limpar), que no windows é chamada cls.
import os

os.system("cls")
print("================= Criar Diretório =================")
os.mkdir("criado_pelo_python")
print("Diretório criado")
