#DIA 1: PROGRAMA PARA CALCULAR IMC

print("\n---CALCULADORA DE IMC---") #PRINT DO OBJETIVO DO PROGRAMA

nome = str(input("Digite seu nome: ")).upper() #LÊ O NOME DA PESSOA (EM STRING) E TRANSFORMA TODAS AS LETRAS EM MAIÚSCULA

massa = float(input("Digite sua massa corporal: ")) #LÊ A MASSA CORPORAL DA PESSOA (EM FLOAT)

altura = float(input("Digite sua altura: ")) #LÊ A ALTURA DA PESSOA (EM FLOAT)

def calculo_imc(massa, altura): #CRIAÇÃO DE UMA FUNÇÃO PASSANDO DOIS PARÂMETROS: A MASSA E A ALTURA DA PESSOA
    return (massa / (altura ** 2)) #RETORNA O CÁLCULO DO IMC

imc = calculo_imc(massa, altura) #NA MAIN, ATRIBUI O CÁLCULO REALIZADO NA FUÇÃO AO IMC


#PRINTA OS DADOS DA PESSOA
print("\n---SEUS DADOS---")
print("Seu nome:", nome)
print("Sua massa corporal:", massa, "kg")
print("Sua altura:", altura, "m")
print("Com base em seus dados, seu IMC é:", round(imc, 2)) #TRANSFORMA O IMC EM SOMENTE DUAS CASAS DECIMAIS

print("\n---CLASSIFICAÇÃO---") #USO DE CONDICIONAIS PARA CLASSIFICAR O IMC DA PESSOA

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")