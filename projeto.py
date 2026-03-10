entrada = input("Escreva o texto: ")
numero = int(input("Escreva quantas vezes que quer imprimir o texto: "))

for i in range(1, numero+1):
    print(f"{entrada} | {i}")