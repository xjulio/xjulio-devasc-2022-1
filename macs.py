arquivo = open("macs.txt")
saida = arquivo.readlines()
print(saida)
print(type(saida))
print(len(saida))
arquivo.close()
