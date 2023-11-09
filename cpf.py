cpf = input("Digite seu CPF: ")

cpf_tratado = [int(x) for x in cpf.replace(".", "").replace("-", "")]

acc = 0
for x in range(9):
    acc+=cpf_tratado[x]*(10-x)

digito1 = acc*10 % 11
digito1 = digito1 if digito1 <= 9 else 0

acc = 0
for x in range(10):
    acc+=cpf_tratado[x]*(11-x)

digito2 = acc*10 % 11
digito2 = digito2 if digito2 <= 9 else 0

print(f'{cpf}{" não" if digito1 != cpf_tratado[-1] or digito2 != cpf_tratado[-2] else ""} é válido')