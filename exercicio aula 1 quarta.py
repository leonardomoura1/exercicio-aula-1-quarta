import os
import random
#ordenação de numeros decrecente
#escrever 5 input e a saida e ordena os input

banco = []
banco_ordenado = []
count = 1
while True:
    try:
        print("Deseja ordenar em ordem crescente ou decrescente ?")
        print("crecente = 1 , decrescente = 2 , sair = 3")
        ordem = int(input(": "))#escolher qual ordem a pessoa deseja
        if ordem == 3:
            break
        elif ordem >3:#caso a pessoa digite um numero maior que 3 avisar que a opção é invalida e limpar tela
            os.system('cls')
            print("opção invalida")
            input("pressione enter para continuar\n")
            continue
        print('''Deseja ordenar numeros ou letras ?''')
        variavel = int(input("numeros = 1 , letras = 2 : "))#escolher se a pessoa deseja ordenar numeros ou letras
        if variavel > 2:
            os.system('cls')
            print("opção invalida")
            input("pressione enter para continuar\n")
            continue
        quant = int(input("Quantos dados deseja inserir: "))#quantidade de dados que a pessoa deseja inserir
            
        while count <= quant:#loop para inserir os dados na lista
            if variavel == 1:
                valor = int(input("digite um numero: "))
                print()
                banco.append(valor)
                count += 1
            elif variavel == 2:
                valor = input("digite algo: ")
                print()
                banco.append(valor)
                count += 1

        posicao = 0
        for i in range(len(banco)):#loop para criar uma lista com o mesmo tamanho da lista banco
            banco_ordenado.append(0)

        for i in range(len(banco)):#loop para ordenar os dados
            valor1 = banco[i]#valor1 recebe o valor da lista banco
            for k in range(len(banco)):#loop para comparar os valores da lista banco
                valor2 = banco[k]
                if ordem == 1:#condição para saber qual ordem a pessoa deseja
                    if valor1 > valor2:
                        posicao += 1  #posição recebe +1 para que o valor1 seja inserido na posição correta 
                    else:
                        pass
                elif ordem == 2:
                    if valor1 < valor2:
                        posicao += 1   
                    else:
                        pass
            banco_ordenado[posicao] = valor1#valor1 e inserido na posição correta
            posicao = 0#posição recebe 0 para recomeçar o processo para o proximo valor da lista banco

        print(banco_ordenado,'\n')#printar a lista ordenada
        break
    except:
        os.system('cls')#caso a pessoa digite um valor que não seja numero avisar que a opção é invalida e limpar tela
        print("Apenas numero e aceito")
        input("pressione enter para continuar\n")

input("pressione enter para iniciar o proximo exercicio\n")
os.system('cls')
# criar unma logica quantos kilometros  faz com litro

carros = [['skyline'], ['viper'], ['bmw'], ['ferrari']]#lista com os nomes dos carros que tem salvo no banco de dados

print('''escolha um carro para saber quantos kilometros ele faz com um litro de combustivel
baseado no consumo de cada carro
basta digitar o numero do carro que deseja saber
começando do 0 ate 3 na ordem da lista abaixo\n''')

print(carros,'\n')#printar a lista com os nomes dos carros

for i in range(len(carros)):#loop para adicionar os valores de km/litro de cada carro
    carros[i].append(random.randint(5, 20))#adiciona um valor aleatorio de 5 a 20 na lista carros para ser o km/litro do carro

carro = int(input('digite o numero do carro: '))#input para escolher o carro que deseja saber quantos km ele faz com um litro de combustivel

litros = int(input('\nquantos litros de combustivel tem o carro: '))#input para saber quantos litros de combustivel tem o carro

carro_km = carros[carro][1]#carro_km recebe o valor de km/litro do carro escolhido

km_litro = carro_km * litros#km_litro recebe o valor de km/litro do carro escolhido multiplicado pelo valor de litros que o carro tem

print('O carro roda {} km com {} litros de combustivel'.format(km_litro,litros))#printa o valor de km que o carro faz com o valor de litros que o carro tem

