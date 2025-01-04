def operacao_matematica():
    # Solicitar entrada de dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Solicitar a operação desejada
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Realizar a operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = abs(num1 - num2)
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero não é permitida."
    else:
        resultado = "Operação inválida."

    # Exibir o resultado
    print(f"O resultado da operação é: {resultado}")

if __name__ == "__main__":
    operacao_matematica()