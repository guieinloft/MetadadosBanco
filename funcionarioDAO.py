from funcionario import Funcionario
import conexao

class FuncionarioDAO:
    def __init__(self):
        pass


    def inserir(self, idFunc, nome, cpf, nasc, salario):
        sql = "insert into Funcionario (idFunc, nome, cpf, nasc, salario) values (%s, %s, %s, %s, %s)"
        with conexao.abrir("db") as con:
            cur = con.cursor()
            cur.execute(sql, (idFunc, nome, cpf, nasc, salario))
            con.commit()
            return cur.lastrowid  # Supondo que você quer retornar o ID gerado

    def buscar(self, idFunc):
        sql = "select * from Funcionario where idFunc = %s"
        with conexao.abrir("db") as con:
            cur = con.cursor()
            cur.execute(sql, (idFunc,))
            row = cur.fetchone()
            if row:
                return Funcionario(*row)
            return None


    def alterar(self, funcionario):
        sql = "update Funcionario set nome = %s, cpf = %s, nasc = %s, salario = %s where idFunc = %s"
        with conexao.abrir("db") as con:
            cur = con.cursor()
            cur.execute(sql, (funcionario.getnome(), funcionario.getcpf(), funcionario.getnasc(), funcionario.getsalario(), funcionario.getidFunc()))
            con.commit()


    def remover(self, funcionario):
        sql = "delete from Funcionario where idFunc = %s"
        with conexao.abrir("db") as con:
            cur = con.cursor()
            cur.execute(sql, (funcionario.getidFunc(),))
            con.commit()


    def buscartodos(self):
        sql = "select * from Funcionario"
        with conexao.abrir("db") as con:
            cur = con.cursor()
            cur.execute(sql)
            lista = []
            for row in cur:
                lista.append(Funcionario(*row))
            return lista

