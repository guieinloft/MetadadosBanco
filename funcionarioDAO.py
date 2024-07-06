from funcionario import Funcionario
import conexao

class FuncionarioDAO:
    def __init__(self):
        pass


    def inserir(self, idFunc, nome, cpf, nasc, salario):
        sql = "insert into funcionario(idFunc, nome, cpf, nasc, salario) values (%s, %s, %s, %s, %s)"
        with conexao.abrir(test) as con:
            cur = con.cursor()
            cur.execute(sql, (idFunc, nome, cpf, nasc, salario))


    def buscar(self, idFunc):
        sql = "select * from funcionariowhere idFunc = %s"
        with conexao.abrir(test) as con:
            cur = con.cursor()
            cur.execute(sql, (idFunc,))
            return Funcionario(cur[0], cur[1], cur[2], cur[3], cur[4])


    def alterar(self, func):
        sql = "update funcionario set nome = %s, cpf = %s, nasc = %s, salario = %s where idFunc = %s"
        with conexao.abrir(test) as con:
            cur = con.cursor()
            cur.execute(sql, (func.getnome(), func.getcpf(), func.getnasc(), func.getsalario(), func.getidFunc(),))


    def remover(self, func):
        sql = "delete funcionario where idFunc = %s"
        with conexao.abrir(test) as con:
            cur = con.cursor()
            cur.execute(sql, (func.getidFunc(),))


    def buscartodos(self):
        sql = "select * from funcionario"
        with conexao.abrir(test) as con:
            cur = con.cursor()
            cur.execute(sql)
            listfunc = list()
            for func in cur:
                listfunc.append(Funcionario(cur[0], cur[1], cur[2], cur[3], cur[4]))
            return listfunc


