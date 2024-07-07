class Funcionario:
    def __init__(self, idFunc, nome, cpf, nasc, salario):
        self.__idFunc = idFunc # int
        self.__nome = nome # varchar(255)
        self.__cpf = cpf # varchar(20)
        self.__nasc = nasc # date
        self.__salario = salario # decimal(8,2)


    def getidFunc(self):
        return self.__idFunc


    def setidFunc(self, idFunc):
        self.__idFunc = idFunc


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


    def getsalario(self):
        return self.__salario


    def setsalario(self, salario):
        self.__salario = salario


