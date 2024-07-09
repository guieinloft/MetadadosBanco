from funcionario import Funcionario
from funcionarioDAO import FuncionarioDAO
import random
import string

def generate_random_value(data_type):
    if data_type.startswith('int'):
        return random.randint(1, 1000)
    elif data_type.startswith('decimal') or data_type.startswith('float'):
        return round(random.uniform(1.0, 1000.0), 1)
    elif data_type.startswith('varchar'):
        length = int(data_type.split('(')[1].strip(')'))
        return ''.join(random.choices(string.ascii_letters + string.digits, k=min(length, 20)))
    elif data_type == 'date':
        year = random.randint(1950, 2003)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f'{year}-{month:02d}-{day:02d}'
    else:
        return None


def main():
    example = Funcionario(generate_random_value('int(11)'), generate_random_value('varchar(255)'), generate_random_value('varchar(20)'), generate_random_value('date'), generate_random_value('decimal(8,2)'))

    dao = FuncionarioDAO()
    # Inserir exemplo
    dao.inserir(example.getidFunc(), example.getnome(), example.getcpf(), example.getnasc(), example.getsalario())
    print(f'{example} foi inserido')

    # Buscar exemplo
    buscado = dao.buscar(example.getidFunc())
    print(f'{buscado} foi buscado')

    # Alterar exemplo
    example.setnome(generate_random_value('varchar(255)'))
    dao.alterar(example)
    print(f'{example} foi alterado')

    # Buscar todos os exemplos
    todos = dao.buscartodos()
    for item in todos:
        print(item)

    # Remover exemplo
    # dao.remover(example)
    # print(f'{example} foi removido')

if __name__ == '__main__':
    main()
