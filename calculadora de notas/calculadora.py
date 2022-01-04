nota1 = float(input("Primeira avaliação:"))
nota2 = float(input("Segunda avaliação:"))
nota3 = float(input("Terceira avaliação:"))
nota4 = float(input("Quarta avaliação:"))

média = (nota1+nota2+nota3+nota4)/4
print ("==" * 12)

if média >= 5 and média < 7:
    print("Status= Recuperação")
elif média < 5:
    print("Status= Reprovado")
elif média >= 7:
    print("status= Aprovado")
