from funcionario import Funcionario
import conexao

class FuncionarioDAO:
    def __init__(self):
        pass


    def inserir(self, idFunc, nome, cpf, nasc, salario):
        sql = "insert into funcionario(idFunc, nome, cpf, nasc, salario) values (%s, %s, %s, %s, %s)"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (idFunc, nome, cpf, nasc, salario))
            con.commit()


    def buscar(self, idFunc):
        sql = "select * from funcionario where idFunc = %s"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (idFunc,))
            result = cur.fetchone()
            if result is not None:
                return Funcionario(result[0], result[1], result[2], result[3], result[4])
            else:
                return None


    def alterar(self, func):
        sql = "update funcionario set nome = %s, cpf = %s, nasc = %s, salario = %s where idFunc = %s"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (func.getnome(), func.getcpf(), func.getnasc(), func.getsalario(), func.getidFunc(),))
            con.commit()


    def remover(self, func):
        sql = "delete from funcionario where idFunc = %s"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (func.getidFunc(),))
            con.commit()


    def buscartodos(self):
        sql = "select * from funcionario"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql)
            listfunc = list()
            for row in cur:
                listfunc.append(Funcionario(row[0], row[1], row[2], row[3], row[4]))
            return listfunc


