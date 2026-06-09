# Pedir ao usuário a entrada dos numeros do CPF e guarda a variavel
# cpf_original. Aqui o usuário digitará o cpf completo.
cpf_original = input("Digite seu CPF, apenas números:")

# Ajuda a contar os numeros do CPF laço while.
i = 0


# Guarda os 9 primeiros digitos do CPF.
cpf_nove = ""

# Enquanto(while) o valor de i for maior ou menor que 9, neste caso, irá até 8
# vai pegando um número por vez no cpf_original(digitado pelo usuário com
# 11 digitos) e vai adicionando, um ao lado do outro, na variavel cpf_9.
# A ideia é obter os 9 primeiros digitos.

while i < 9:
    cpf_nove+=cpf_original[i]
    i+=1
print(cpf_nove)

# Para calcular o primeiro digito verificador, iremos usar cada número do
# cpf_nove multiplicado pelo peso que vai de 10 a 2.
peso = 10

# A variavel resultado é utilizada para guarda a soma do resultado da
# multiplicação.

resultado = 0

# Variavel i é usada para obter um numero por vez do cpf_nove.
i = 0
while i < 9:
    # A variável resultado soma os resultados obtidos da multiplicação
    # dos números do CPF com peso. Como a variável cpf_nove é uma cadeia
    # de string, será necessário converter cada número obtido para inteiro
    # com comando int

    resultado+=int(cpf_nove[i]) * peso
    # peso -= 1, diminuir em 1 o valor do peso, passando de 10 para 9, depois
    # para 8 e assim por diante até chegar em 2
    peso-=1

    # A variável i, que inicia com 0, deve ser incrementada em 1(i+=1) para
    # sair de zero(0) e chegar em 8. Assim a cada vez que o laço roda(executa)
    # o valor de i é incrementado em 1, então ele, i, vai para 1 depois 2
    # e assim por diante até chegar em 9(sendo 9 o ponto de saída)

    i+=1
print(resultado)

# A variavel resto guarda o resultado do cálculo entre o resultado, que
# foi obtido dentro do laço while com o numero 11. Nesta operação estamos
# obtendo o resto da divisão, por isso, usamos  o operado %.
# se o resto da divisão for menor que 2, então o primeiro digito
# verificador é zero(0). Note que ele está entre aspas, pois queremos
# juntar com os outros números que estão dentro da variável cpf-nove, que
# também são characteres.
# Caso o resultado do cálculo resulte em numero mair que 2, então faz-se
# a subtração de 11 por resto, que é o resultado do cálculo. Para manter
# o valor em formato string, estamos usando o comando str(string)     
resto = resultado % 11
if resto < 2:
    cpf_nove +="0"
else:
    cpf_nove += str(11-resto)
print(cpf_nove)

peso = 11
resultado = 0
i = 0
while i < 10:
    resultado+=int(cpf_nove[i]) * peso
    peso-=1
    i+=1
print(resultado)
resto = resultado % 11
if resto < 2:
    cpf_nove +="0"
else:
    cpf_nove += str(11-resto)
print(cpf_nove)

if cpf_nove == cpf_original:
    print("CPF Valido!")
else:
    print("CPF Invalido!")