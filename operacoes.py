n1 = input("Digite um numero;")
n2 = input("Digite outro numero;")

# Para realizar as operações aritimeticas, ser
# necessário converter as variaveis n1 e n2 e em
# tipos numericos, que podem ser int ou float

n1 = int(n1)
n2 = int(n2)

soma = n1 + n2
subtrair = n1 - n2
multiplicar = n1 * n2
dividir = n1 / n2
print(f"A soma entre os numeros {n1} e {n2} é {soma}")
print(f"A subtração entre os numeros {n1} e {n2} é {subtrair}")
print(f"A multiplicação entre os numeros {n1} e {n2} é {multiplicar}")
print(f"A divisão entre os numeros {n1} e {n2} é {dividir}")