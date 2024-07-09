class Cliente:
    def __init__(self, idCliente, nome, cpf, nasc):
        self.__idCliente = idCliente # int(11)
        self.__nome = nome # varchar(255)
        self.__cpf = cpf # varchar(20)
        self.__nasc = nasc # date


    def getidCliente(self):
        return self.__idCliente


    def setidCliente(self, idCliente):
        self.__idCliente = idCliente


    def getnome(self):
        return self.__nome


    def setnome(self, nome):
        self.__nome = nome


    def getcpf(self):
        return self.__cpf


    def setcpf(self, cpf):
        self.__cpf = cpf


    def getnasc(self):
        return self.__nasc


    def setnasc(self, nasc):
        self.__nasc = nasc


