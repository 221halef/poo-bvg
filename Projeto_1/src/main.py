from models.cliente import Cliente

if __name__ == "__main__":
    cliente1 = Cliente("João Silva", 30, 1000.0)
    cliente2 = Cliente("Maria Souza", 25, 500.0)

    lista_clientes = [cliente1, cliente2]

    try:
        cliente1.sacar(1500.0)
    except ValueError as erro:
        print(f"Erro na transação de {cliente1.nome}: {erro}")

    try:
        cliente2.depositar(250.0)
    except ValueError as erro:
        print(f"Erro na transação de {cliente2.nome}: {erro}")

    print("\n--- RELATÓRIO GERAL ---")
    for index, cliente in enumerate(lista_clientes):
        print(cliente.obter_relatorio(index))
