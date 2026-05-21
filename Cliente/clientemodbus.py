from pymodbus.client import ModbusTcpClient
from time import sleep

class ClienteMODBUS():
    """
    Classe Cliente MODBUS usando pymodbus
    """
    def __init__(self, server_ip, porta, scan_time=1):
        """
        Construtor
        """
        # Cria o cliente TCP
        self._cliente = ModbusTcpClient(host=server_ip, port=porta)
        self._scan_time = scan_time

    def conectar(self):
        """
        Conecta ao servidor MODBUS
        """
        self._cliente.connect()
        
    def write_float(self, endereco, valor = float):
        regs = self._cliente.convert_to_registers(valor, data_type=self._cliente.DATATYPE.FLOAT32)
        resultado = self._cliente.write_registers(address=endereco, values=regs)
        if resultado.isError():
            return False
        return resultado
        
    def read_float(self, endereco):
        regs = self._cliente.read_holding_registers(address=endereco, count=2)
        if regs.isError():
            return None
        resultado = self._cliente.convert_from_registers(regs.registers, data_type=self._cliente.DATATYPE.FLOAT32)
        return resultado

    def holding_register_bits(self, endereco):
        resultado = self._cliente.read_holding_registers(address=endereco, count=1)
        if resultado.isError():
            return None
        valor_int = resultado.registers[0]
        lista_bits = []
        for i in range(16):
            bit = (valor_int >> i) & 1
            lista_bits.append(bit)
        return lista_bits
    
    def write_bits(self, endereco,endereco_bits, valor):
        ler_bits = self._cliente.read_holding_registers(address=endereco,count=1)
        if ler_bits.isError():
            return False
        valor_int = ler_bits.registers[0]
        if valor == 1:
            novo_valor = valor_int | (1 << endereco_bits)
        else:
            novo_valor = valor_int & ~(1 << endereco_bits)
        resultado = self._cliente.write_registers(address=endereco, values=[novo_valor])
        if resultado.isError():
            return False
        return True
    