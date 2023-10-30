termo1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

for i in range(10) :
    print(i)
    termo = termo1 + i * razao
    print(f"Termo {i+1}: {termo}")