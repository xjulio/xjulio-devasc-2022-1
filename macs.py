with open("macs.txt", "r", encoding="utf-8") as arquivo:
    while linha := arquivo.readline():
        print(linha)
        linha = arquivo.readline()
