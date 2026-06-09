def calcular_digito(cpf_parcial):
    soma = sum(
        int(numero) * peso
        for numero, peso in zip(
            cpf_parcial,
            range(len(cpf_parcial) + 1, 1, -1)
        )
    )

    resto = soma % 11
    return "0" if resto < 2 else str(11 - resto)


cpf = input("CPF: ").strip()

if (
    len(cpf) == 11
    and cpf.isdigit()
    and cpf != cpf[0] * 11
):
    cpf_gerado = cpf[:9]
    cpf_gerado += calcular_digito(cpf_gerado)
    cpf_gerado += calcular_digito(cpf_gerado)

    print("CPF válido!" if cpf_gerado == cpf else "CPF inválido!")
else:
    print("CPF inválido!")