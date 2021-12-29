import matplotlib.pyplot as grafico

meses = []
casos = []

arquivo = open('dados', 'r')
for linha in arquivo:
    linha = linha.split("/")
    mes = linha[0]
    meses.append(mes)

    caso = int(linha[1])
    casos.append(caso)

grafico.title('Covid - Brasil 2020')
grafico.ylabel('Casos')
grafico.xlabel('Meses')
grafico.plot(meses, casos, label='Casos', marker = 'o')
grafico.legend()
grafico.show()


    