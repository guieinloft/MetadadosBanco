import conexao

def writeClass(table, columns):
    filename = "./" + table + ".py"
    cnames = list()
    pkeys = list()
    for column in columns:
        cnames.append(column[0])
        if "PRI" in column[3]:
            pkeys.append(column[0])
    with open(filename, "w", encoding="utf-8") as f:
        f.write("class " + table.title() + ":\n")
        
        # criando construtor (com atributos null)
        f.write("    def __init__(self" + (", " if len(cnames) > 0 else "") + ", ".join(cnames) + "):\n")
        for column in columns:
            f.write("        self.__" + column[0] + " = " + column[0] + " # " + column[1] + "\n")
        
        f.write("\n\n")

        # criando getters e setters
        for column in columns:
            f.write("    def get" + column[0] + "(self):\n        return self.__" + column[0] + "\n\n\n")
            f.write("    def set" + column[0] + "(self, " + column[0] + "):\n"
                    + "        self.__" + column[0] + " = " + column[0] + "\n\n\n")


def writeDAO(database, table, columns):
    filename = "./" + table + "DAO.py"
    cnames = list()
    pkeys = list()
    notpk = list()
    for column in columns:
        cnames.append(column[0])
        if "PRI" in column[3]:
            pkeys.append(column[0])
        else:
            notpk.append(column[0])

    with open(filename, "w", encoding = "utf-8") as f:
        f.write("from " + table + " import " + table.title() + "\n")
        f.write("import conexao\n\n")
        f.write("class " + table.title() + "DAO:\n")

        # criando construtor
        f.write("    def __init__(self):\n        pass\n\n\n")

        # criando insercao
        f.write("    def inserir(self" + (", " if len(cnames) > 0 else "") + ", ".join(cnames) + "):\n")
        f.write("        sql = \"insert into " + table + "(" + ", ".join(cnames) +
                ") values (" + ("%s, " * (len(cnames) - 1)) + "%s)\"\n")
        f.write("        with conexao.abrir(\"" + database + "\") as con:\n")
        f.write(" "*12 + "cur = con.cursor()\n")
        f.write(" "*12 + "cur.execute(sql, (" + ", ".join(cnames) + ("," if len(cnames) == 1 else "") + "))\n\n\n")
        
        # criando busca
        f.write("    def buscar(self, " + ", ".join(pkeys) + "):\n")
        f.write("        sql = \"select * from " + table + "where " + " = %s and ".join(pkeys) + " = %s\"\n")
        f.write("        with conexao.abrir(\"" + database + "\") as con:\n")
        f.write(" "*12 + "cur = con.cursor()\n")
        f.write(" "*12 + "cur.execute(sql, (" + ", ".join(pkeys) + ("," if len(pkeys) == 1 else "") + "))\n")
        f.write(" "*12 + "return " + table.title() + "(")
        for i in range(len(cnames)-1):
            f.write("cur[" + str(i) + "], ")
        f.write("cur[" + str(len(cnames)-1) + "])\n\n\n")

        # criando alteracao
        methodsnk = list()
        methodspk = list()
        for column in notpk:
            methodsnk.append(table[:4] + ".get" + column + "()")
        for column in pkeys:
            methodspk.append(table[:4] + ".get" + column + "()")
        f.write("    def alterar(self, " + table[:4] + "):\n")
        f.write("        sql = \"update " + table + " set " + " = %s, ".join(notpk) + " = %s where " + " = %s and ".join(pkeys) + " = %s\"\n")
        f.write("        with conexao.abrir(\"" + database + "\") as con:\n")
        f.write(" "*12 + "cur = con.cursor()\n")
        f.write(" "*12 + "cur.execute(sql, (" + ", ".join(methodsnk) + ", " + ", ".join(methodspk) + ("," if len(methodspk) == 1 else "") + "))\n\n\n")

        # criando remocao
        f.write("    def remover(self, " + table[:4] + "):\n")
        f.write("        sql = \"delete " + table + " where " + " = %s and ".join(pkeys) + " = %s\"\n")
        f.write("        with conexao.abrir(\"" + database + "\") as con:\n")
        f.write(" "*12 + "cur = con.cursor()\n")
        f.write(" "*12 + "cur.execute(sql, (" + ", ".join(methodspk) + ("," if len(methodspk) == 1 else "") + "))\n\n\n")

        # criando buscar todos
        f.write("    def buscartodos(self):\n")
        f.write("        sql = \"select * from " + table + "\"\n")
        f.write("        with conexao.abrir(\"" + database + "\") as con:\n")
        f.write(" "*12 + "cur = con.cursor()\n")
        f.write(" "*12 + "cur.execute(sql)\n")
        f.write(" "*12 + "list" + table[:4] + " = list()\n")
        f.write(" "*12 + "for " + table[:4] + " in cur:\n")
        f.write(" "*16 + "list" + table[:4] + ".append(" + table.title() + "(")
        for i in range(len(cnames)-1):
            f.write("cur[" + str(i) + "], ")
        f.write("cur[" + str(len(cnames)-1) + "]))\n")
        f.write(" "*12 + "return list" + table[:4] + "\n\n\n")


def main():
    database = input('Digite o nome do banco: ')
    with conexao.abrir(database) as con:
        cur = con.cursor()
    
        queryt = 'show tables'
        tables = list()
    
        cur.execute(queryt)
        for table in cur:
            tables.append(table[0])
    
        for table in tables:
            queryc = 'describe ' + table
            cur.execute(queryc)
            columns = list()
            pkeys = list()
            for column in cur:
                columns.append(column)

            writeClass(table, columns)
            writeDAO(database, table, columns)


if __name__ == "__main__":
    main()
