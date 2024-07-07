from faker import Faker
from funcionarioDAO import FuncionarioDAO
from funcionario import Funcionario

# Instanciar Faker
faker = Faker()

# Instanciar DAO
funcionario_dao = FuncionarioDAO()

# Criar um funcionário fictício com idFunc como None
funcionario = Funcionario(
    idFunc=None,  # Será gerado automaticamente pelo banco de dados
    nome=faker.name(),
    cpf=faker.ssn(),  # Use faker-extended para CPF brasileiro
    nasc=faker.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d'),
    salario=round(faker.random_number(digits=5) / 100, 2)
)

# Demonstrar operações CRUD
# Criar
id_gerado = funcionario_dao.inserir(
    funcionario.getidFunc(),
    funcionario.getnome(),
    funcionario.getcpf(),
    funcionario.getnasc(),
    funcionario.getsalario()
)
funcionario.setidFunc(id_gerado)  # Atualizar o ID do funcionário com o ID gerado
print(f'Criado: {funcionario}')

# Ler
funcionario_lido = funcionario_dao.buscar(funcionario.getidFunc())
print(f'Lido: {funcionario_lido}')

# Atualizar
funcionario.setnome(faker.name())
funcionario_dao.alterar(funcionario)
funcionario_atualizado = funcionario_dao.buscar(funcionario.getidFunc())
print(f'Atualizado: {funcionario_atualizado}')

# Deletar
funcionario_dao.remover(funcionario)
print(f'Funcionário com ID {funcionario.getidFunc()} deletado.')

# Buscar todos (para verificar se está vazio após a remoção)
todos_funcionarios = funcionario_dao.buscartodos()
print(f'Todos os funcionários: {todos_funcionarios}')
