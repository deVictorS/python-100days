#DIA 2: CÁLCULO DE MÉDIA DE NOTAS

print("\n---CÁLCULO APROVAÇÃO/REPROVAÇÃO---") #PRINT DO OBJETIVO DO PROGRAMA

#SOLICITA OS DADOS AO USUÁRIO E OS ARMAZENA EM VARIÁVEIS DO TIPO FLOAT
nota1 = float(input("\nDIGITE A NOTA DA SUA PRIMEIRA PROVA: "))
nota2 = float(input("DIGITE A NOTA DA SUA SEGUNDA PROVA: "))
nota3 = float(input("DIGITE A NOTA DA SUA TERCEIRA PROVA: "))


#FUNÇÃO QUE CALCULA A MÉDIA DAS NOTAS E RETORNA A MESMA
def calculoNotas(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

#ATRIBUI O VALOR CALCULADO NA FUNÇÃO À VARIÁVEL 
media_final = calculoNotas(nota1, nota2, nota3)

print("\nSUA MÉDIA FINAL É:", round(media_final, 2)) #PRINTA O CÁLCULO DA MÉDIA COM DUAS CASAS DECIMAIS

#CUSO DE CONDICIONAIS PARA CLASSIFICAR A MÉDIA
if media_final >= 6:
    print("VOCÊ FOI APROVADO")

elif 6 > media_final >= 5:
    print("VOCÊ PODE REALIZAR A RECUPERAÇÃO")

else:
    print("VOCÊ FOI REPROVADO")    


