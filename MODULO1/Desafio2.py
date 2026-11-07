nota1 = 8
nota2 = 9
nota3 = 6
nota4 = 8
media = (nota1 + nota2 + nota3 + nota4)/4
print(f"A média do aluno é: {media:.1f}")

if media > 7:
    print("Aprovado")
if media >= 5:
    print("Recuperação")
if media < 5:
    print("Reprovado")