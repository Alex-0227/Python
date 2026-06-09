qtd = 0
for a in range (1950,2027):
        if a % 4 == 0:
                print(f"O ano {a} bissexto")
                qtd+=1
print("----------------------")
print(f"Quantidade de anos bissextos e {qtd}")