class Gato:
    def __init__(self,raca: str,cor: str,tipo_pelo: str,idade: int,name: str):
        """
        Docstring for __init__
        
        :param self: Comando que faz os atributos e métodos olharem para a classe
        :param raca: Digite a raça do gato (EX: Siamês, Siberian, Ragdoll, Persa...)
        :type raca: str
        :param cor: Digite a cor do gato
        :type cor: str
        :param tipo_pelo: Digite o tipo de pelo (EX: Sem pelo, pelo longo, pelo curto)
        :type tipo_pelo: str
        :param idade: Digite a idade do gato
        :type idade: int
        :param name: Digite o nome do gato
        :type name: str

        """
        self.name = name
        self.idade = idade
        self.raca = raca
        self.cor = cor
        self.tipo_pelo = tipo_pelo

    def miar(self):
        print(f"O {self.name} sorriu")

meu_gato = Gato("Darkner","preto","Pelo Longo",7,"FRIEND")
meu_gato.miar()





print(f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⢀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⣼⣿⣿⣿⣦⠀⠀⠀⠀⠀⢠⣼⣿⡿⡿⣿⡆⠀⠀⣿⡆⠀
⠀⠀⢸⣧⠀⠀⢸⣿⣿⣿⣇⣀⡹⠀⠀⠀⠀⠀⢸⣿⣿⣇⡀⣿⠆⠀⠀⣿⠇⠀
⠀⠀⠸⣿⡇⠀⠈⠻⠿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠈⠿⠿⠿⠛⠃⠀⣀⣼⡿⠀⠀
⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀
⠀⠀⠀⠈⢿⣿⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣄⣈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⣿⣿⡆⢠⣶⣶⣶⣶⣶⠀⠀⣰⣶⡀⠘⣿⣿⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣇⠀⠹⣿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⡆⠀⠹⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠿⣿⡇⢸⣿⣿⣿⣿⡇⣤⣾⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠸⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ """)
