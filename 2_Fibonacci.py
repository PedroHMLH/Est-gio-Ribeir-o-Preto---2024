def verifica_fibonacci(numero):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    fib1, fib2 = 0, 1
    
    # Verifica se o número informado é 0 ou 1
    if numero == 0 or numero == 1:
        return True
    
    # Inicia um loop para calcular a sequência de Fibonacci até ultrapassar o número informado
    while fib2 <= numero:
        # Se o número informado for igual a algum número na sequência, retorna True
        if fib2 == numero:
            return True
        # Calcula o próximo número na sequência de Fibonacci
        fib1, fib2 = fib2, fib1 + fib2
    
    # Se o número não for encontrado na sequência, retorna False
    return False

# Número a ser verificado
numero_verificar = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Chama a função e imprime o resultado
if verifica_fibonacci(numero_verificar):
    print(f"O número {numero_verificar} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_verificar} não pertence à sequência de Fibonacci.")
def verifica_fibonacci(numero):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    fib1, fib2 = 0, 1
    
    # Verifica se o número informado é 0 ou 1
    if numero == 0 or numero == 1:
        return True
    
    # Inicia um loop para calcular a sequência de Fibonacci até ultrapassar o número informado
    while fib2 <= numero:
        # Se o número informado for igual a algum número na sequência, retorna True
        if fib2 == numero:
            return True
        # Calcula o próximo número na sequência de Fibonacci
        fib1, fib2 = fib2, fib1 + fib2
    
    # Se o número não for encontrado na sequência, retorna False
    return False

# Número a ser verificado
numero_verificar = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Chama a função e imprime o resultado
if verifica_fibonacci(numero_verificar):
    print(f"O número {numero_verificar} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_verificar} não pertence à sequência de Fibonacci.")
