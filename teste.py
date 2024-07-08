import conexao
import random
import string



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
        f.write("        sql = \"select * from " + table + " where " + " = %s and ".join(pkeys) + " = %s\"\n")
        f.write("        with conexao.abrir(\"" + database + "\") as con:\n")
        f.write(" "*12 + "cur = con.cursor()\n")
        f.write(" "*12 + "cur.execute(sql, (" + ", ".join(pkeys) + ("," if len(pkeys) == 1 else "") + "))\n")
        f.write(" "*12 + "result = cur.fetchone()\n")
        f.write(" "*12 + "if result is not None:\n")
        f.write(" "*16 + "return " + table.title() + "(")
        for i in range(len(cnames)-1):
            f.write("result[" + str(i) + "], ")
        f.write("result[" + str(len(cnames)-1) + "])\n")
        f.write(" "*12 + "else:\n")
        f.write(" "*16 + "return None\n\n\n")

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
        f.write("        sql = \"delete from " + table + " where " + " = %s and ".join(pkeys) + " = %s\"\n")
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
        f.write(" "*12 + "for row in cur:\n")
        f.write(" "*16 + "list" + table[:4] + ".append(" + table.title() + "(")
        for i in range(len(cnames)-1):
            f.write("row[" + str(i) + "], ")
        f.write("row[" + str(len(cnames)-1) + "]))\n")
        f.write(" "*12 + "return list" + table[:4] + "\n\n\n")


def create_example_file(table, columns):
    filename = f"{table}Exemplo.py"
    class_name = table.title()
    dao_class_name = class_name + "DAO"
    imports = f"from {table} import {class_name}\nfrom {table}DAO import {dao_class_name}\nimport random\nimport string\n\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(imports)
        f.write("def generate_random_value(data_type):\n")
        f.write("    if data_type.startswith('int'):\n")
        f.write("        return random.randint(1, 1000)\n")
        f.write("    elif data_type.startswith('decimal'):\n")
        f.write("        return round(random.uniform(1.0, 1000.0), 2)\n")
        f.write("    elif data_type.startswith('varchar'):\n")
        f.write("        length = int(data_type.split('(')[1].strip(')'))\n")
        f.write("        return ''.join(random.choices(string.ascii_letters + string.digits, k=min(length, 20)))\n")
        f.write("    elif data_type == 'date':\n")
        f.write("        year = random.randint(1950, 2003)\n")
        f.write("        month = random.randint(1, 12)\n")
        f.write("        day = random.randint(1, 28)\n")
        f.write("        return f'{year}-{month:02d}-{day:02d}'\n")
        f.write("    else:\n")
        f.write("        return None\n\n")

        f.write(f"def main():\n")
        f.write(f"    dao = {dao_class_name}()\n")
        
        # Criar exemplo
        f.write(f"    example = {class_name}(")
        for column in columns:
            f.write(f"generate_random_value('{column[1]}'), ")
        f.seek(f.tell() - 2, 0)
        f.write(")\n\n")
        
        # Inserir exemplo
        f.write(f"    # Inserir exemplo\n")
        f.write(f"    dao.inserir(")
        for column in columns:
            f.write(f"example.get{column[0]}(), ")
        f.seek(f.tell() - 2, 0)
        f.write(")\n")
        f.write(f"    print(f'{{example}} foi inserido')\n\n")
        
        # Buscar exemplo
        f.write(f"    # Buscar exemplo\n")
        primary_keys = [column[0] for column in columns if 'PRI' in column[3]]
        f.write(f"    buscado = dao.buscar(")
        for pk in primary_keys:
            f.write(f"example.get{pk}(), ")
        f.seek(f.tell() - 2, 0)
        f.write(")\n")
        f.write(f"    print(f'{{example}} foi buscado')\n\n")

        # Alterar exemplo
        f.write(f"    # Alterar exemplo\n")
        f.write(f"    example.set{columns[1][0]}(generate_random_value('{columns[1][1]}'))\n")
        f.write(f"    dao.alterar(example)\n")
        f.write(f"    print(f'{{example}} foi alterado')\n\n")
        
        # Remover exemplo
        f.write(f"    # Remover exemplo\n")
        f.write(f"    dao.remover(example)\n")
        f.write(f"    print(f'{{example}} foi removido')\n\n")
        
        # Buscar todos os exemplos
        f.write(f"    # Buscar todos os exemplos\n")
        f.write(f"    todos = dao.buscartodos()\n")
        f.write(f"    for item in todos:\n")
        f.write(f"        print(item)\n\n")
        
        f.write(f"if __name__ == '__main__':\n")
        f.write(f"    main()\n")



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
            create_example_file(table, columns)


if __name__ == "__main__":
    main()
