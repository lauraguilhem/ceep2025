# calculando a idade de uma pessoa
print("********* Qual sua idade?*********")

from datetime import datetime

def calcular_idade(data_nascimento):
    # Converte a data de nascimento para um objeto datetime
    nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    
    # Data atual
    hoje = datetime.today()
    
    # Calcula a idade
    idade = hoje.year - nascimento.year
    
    # Verifica se a pessoa já fez aniversário este ano
    if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
        idade -= 1
    
    return idade

# Entrada de dados
data_nascimento = input("Digite a data de nascimento (formato: YYYY-MM-DD): ")

# Calcular e exibir a idade
idade = calcular_idade(data_nascimento)
print(f"Sua idade é: {idade} anos")

if idade > 60:
    print("Já pode se aposentar!")
else:
    print("Ainda não pode se aposentar.")
