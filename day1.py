print("\n---CALCULADORA DE IMC---")

nome = str(input("Digite seu nome: ")).upper()

massa = float(input("Digite sua massa corporal: "))

altura = float(input("Digite sua altura: "))

def calculo_imc(massa, altura):
    return (massa / (altura ** 2))

imc = calculo_imc(massa, altura)

print("\n---SEUS DADOS---")
print("Seu nome:", nome)
print("Sua massa corporal:", massa, "kg")
print("Sua altura:", altura, "m")
print("Com base em seus dados, seu IMC é:", round(imc, 2))

print("\n---CLASSIFICAÇÃO---")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")