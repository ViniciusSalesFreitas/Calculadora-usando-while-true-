def calcular(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 == 0:
            return "Erro: divisão por zero"
        return n1 / n2
    else:
        return "Operação inválida"


while True:
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    op = input("Operação (+, -, *, /): ")

    resultado = calcular(n1, n2, op)
    print("Resultado:", resultado)

    while True:
        de_novo = input("Deseja calcular de novo? (s/n): ")
        if de_novo == "s":
            break
        elif de_novo == "n":
            print("Até mais!")
            break
        else:
            print("Digite apenas s ou n.")
    if de_novo == "n":
     break
#falta quebrar o primeiro while true das operaçoes, para isso faço mais uma condição so que essa condição vai ter so o break q vai quebrar o ciclo infinito dos while true.
