from cliente import Cliente
import conexao

class ClienteDAO:
    def __init__(self):
        pass


    def inserir(self, idCliente, nome, cpf, nasc):
        sql = "insert into cliente(idCliente, nome, cpf, nasc) values (%s, %s, %s, %s)"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (idCliente, nome, cpf, nasc))
            con.commit()


    def buscar(self, idCliente):
        sql = "select * from cliente where idCliente = %s"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (idCliente,))
            result = cur.fetchone()
            if result is not None:
                return Cliente(result[0], result[1], result[2], result[3])
            else:
                return None


    def alterar(self, clie):
        sql = "update cliente set nome = %s, cpf = %s, nasc = %s where idCliente = %s"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (clie.getnome(), clie.getcpf(), clie.getnasc(), clie.getidCliente(),))
            con.commit()


    def remover(self, clie):
        sql = "delete from cliente where idCliente = %s"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql, (clie.getidCliente(),))
            con.commit()


    def buscartodos(self):
        sql = "select * from cliente"
        with conexao.abrir("test") as con:
            cur = con.cursor()
            cur.execute(sql)
            listclie = list()
            for row in cur:
                listclie.append(Cliente(row[0], row[1], row[2], row[3]))
            return listclie


