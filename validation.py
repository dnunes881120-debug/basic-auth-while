cont = 0
n = 'DANIEL'
nam = str(input("Digite o Seu nome: "))
while nam not in 'DANIEL':
    nam = str(input("Nome Incorreto! Por favor, digite novamente: ")).upper()
    cont +=1
print(f"{nam} Você foi registrado com sucesso!!", end=' ')
print(f"Foram {cont} Tentativas!!")