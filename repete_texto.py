def repetir_texto(): 
    texto = input("Digite uma string: ")
    numero = int(input("Digite um número inteiro: "))
    resultado = (texto + " ") * numero
    print(resultado)

if __name__ == "__main__":
    repetir_texto()