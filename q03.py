nome = (input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))
if idade > 15:
    print(f'Olá {nome} , você tem {idade} anos e está apto a votar nas eleições deste ano')
else:
 print(f'Olá {nome} , você tem {idade} anos e não está apto a votar nas eleições deste ano')