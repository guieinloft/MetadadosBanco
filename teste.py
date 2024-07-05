import mysql.connector

def writeClass(table, columns):
    filename = "./" + table + ".py"
    nullno = list()
    nullyes = list()
    for column in columns:
        if "NO" == column[2]:
            nullno.append(column[0])
        else:
            nullyes.append(column[0] + "=Null")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("class " + table.title() + ":\n")
        
        # criando construtor (com atributos null)
        f.write("    def __init__(self" + (", " if len(nullno) > 0 else "") + ", ".join(nullno)
                + (", " if len(nullyes) > 0 else "") + ", ".join(nullyes) + "):\n")
        for column in columns:
            f.write("        self.__" + column[0] + " = " + column[0] + "\n")
        
        f.write("\n\n")

        # criando getters e setters
        for column in columns:
            f.write("    def get" + column[0] + "(self):\n        return self.__" + column[0] + "\n\n\n")
            f.write("    def set" + column[0] + "(self, " + column[0] + "):\n"
                    + "        self.__" + column[0] + " = " + column[0] + "\n\n\n")


def writeDAO(table, columns):
    filename = "./" + table + "DAO.py"
    pkeys = list()
    nullno = list()
    nullyes = list()
    for column in columns:
        if "PRI" in column[3]:
            pkeys.append(column[0])
        if "NO" == column[2]:
            nullno.append(column[0])
        else:
            nullyes.append(column[0] + "=Null")

    with open(filename, "w", encoding = "utf-8") as f:
        f.write("from " + table + " import " + table.title() + "\n")
        f.write("import mysql.connector\n\n")
        f.write("class " + table.title() + "DAO:\n")

        # criando construtor
        f.write("    def __init__(self):\n        pass\n\n\n")

        f.write("    def inserir(self" + (", " if len(nullno) > 0 else "") + ", ".join(nullno)
                + (", " if len(nullyes) > 0 else "") + ", ".join(nullyes) + "):\n")



def main():
    database = input('Digite o nome do banco: ')
    con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database=database)
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
        writeDAO(table, columns)

    con.close()


if __name__ == "__main__":
    main()
