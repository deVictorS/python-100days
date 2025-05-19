print("\n---CÁLCULO APROVAÇÃO/REPROVAÇÃO---")

nota1 = float(input("\nDIGITE A NOTA DA SUA PRIMEIRA PROVA: "))
nota2 = float(input("DIGITE A NOTA DA SUA SEGUNDA PROVA: "))
nota3 = float(input("DIGITE A NOTA DA SUA TERCEIRA PROVA: "))

def calculoNotas(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media_final = calculoNotas(nota1, nota2, nota3)

print("\nSUA MÉDIA FINAL É:", round(media_final, 2))

if media_final >= 6:
    print("VOCÊ FOI APROVADO")

elif 6 > media_final >= 5:
    print("VOCÊ PODE REALIZAR A RECUPERAÇÃO")

else:
    print("VOCÊ FOI REPROVADO")    


