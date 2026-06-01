class Cliente:
    """
    Representa um cliente no sistema bancário, encapsulando seus dados e operações.
    """

    def __init__(self, nome, idade, saldo_inicial):
        """
        Inicializa o cliente com atributos privados, garantindo o encapsulamento.
        """
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo_inicial
        self.__status = True

    @property
    def nome(self):
        """Retorna o nome do cliente."""
        return self.__nome

    @property
    def idade(self):
        """Retorna a idade do cliente."""
        return self.__idade

    @property
    def saldo(self):
        """Retorna o saldo atual do cliente."""
        return self.__saldo

    @property
    def status(self):
        """Retorna o status de atividade da conta."""
        return self.__status

    def depositar(self, valor):
        """
        Adiciona um valor ao saldo do cliente caso a conta esteja ativa.
        """
        if not self.__status:
            raise ValueError("Conta inativa.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        
        self.__saldo += valor

    def sacar(self, valor):
        """
        Subtrai um valor do saldo do cliente, impedindo que o saldo fique negativo.
        """
        if not self.__status:
            raise ValueError("Conta inativa.")
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self.__saldo:
            raise ValueError("Operação recusada: Saldo insuficiente para realizar este saque.")
            
        self.__saldo -= valor

    def obter_relatorio(self, id_cliente):
        """
        Retorna uma string formatada com os dados do cliente para a exibição de relatórios.
        """
        return f"ID: {id_cliente} | Nome: {self.__nome} | Idade: {self.__idade} | Saldo: R${self.__saldo:.2f} | Ativo: {self.__status}"
