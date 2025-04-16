
dollar = 5.86
euro = 6.69
operacao = ""

while operacao != "5":
    operacao = input("Escolha uma operação: \n1 - Converter de real para dólar\n2 - Converter de real para euro\n3 - Converter de dólar para real\n4 - Converter de euro para real\n5 - Sair\n")
    if operacao == "1":
        valor = float(input("Digite o valor em real: "))
        resultado = valor * dollar
        print(f"{valor} reais é igual a {resultado:.2f} dólares.")

    elif operacao == "2":
        valor = float(input("Digite o valor em real: "))
        resultado = valor * euro
        print(f"{valor} reais é igual a {resultado:.2f} euros.")

    elif operacao == "3":
        valor = float(input("Digite o valor em dólar: "))
        resultado = valor / dollar
        print(f"{valor} dólares é igual a {resultado:.2f} reais.")

    elif operacao == "4":
        valor = float(input("Digite o valor em euro: "))
        resultado = valor / euro
        print(f"{valor} euros é igual a {resultado:.2f} reais.")

    elif operacao == "5":
        print("Saindo...")
        break

    else:
        print("Operação inválida. Tente novamente.")