print("Exemplo de escrita e leitura de valores float")
from clientemodbus import ClienteMODBUS
c = ClienteMODBUS('localhost',502)
c.conectar()
endereco = 2000
print("Escrevendo 109.67 no endereço", endereco)
c.write_float(endereco, 109.67)
c.read_float(endereco)
print("Valor no enderço agora é:", c.read_float(endereco))
print ("Escrevendo 12.75 no endereço",endereco)
c.write_float(endereco, 12.75)
c.read_float(endereco)
print("Valor no enderço agora é:", c.read_float(endereco))
c._cliente.close()