# Vamos usar uma variavel chamada "nome" para
# guardar o nome do cliente. ultilizaremos também
# o comando input(in -> dentro | put -> por em algum lugar)

nome = input("Digite o seu nome:")
print("Olá, sr(a)."+nome)
print(f"Olá, sr(a). {nome}")


print("Olá, sr(a)."+nome+". Seja bem vindo!")

# O operador +(Mais) foi ultilizado para
# concactenar(juntar) o texto entre aspas("")
# com a variavel "nome"

print(f"Olá, sr(a). {nome}. Seja bem vindo!")

# Abaixo, usamos o comando print com letra
#f(format) para inserir uma variavel no meio
# de uma String. A variavel foi inserida copm chaves ({})
# esta tecnica é chamada de interpolação