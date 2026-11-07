numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Terceiro número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero1 > numero3:
    numero1, numero3 = numero3, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2

print("Ordem crescente:", numero1, numero2, numero3)