from conta import Conta


class ContaPoupanca(Conta):

    def __init__(self, agencia: int, numero: int, saldo: float = 0) -> None:
        super().__init__(agencia, numero, saldo)

    def sacar(self, valor) -> float:
        novo_valor = self.saldo - valor

        if novo_valor >= 0:
            self.saldo = novo_valor
            self.detalhes(f'Saque: R${valor:.2f}')
            return self.saldo

        print(
            f'Não é possível sacar o valor desejado. Seu saldo atual é: {self.saldo}')
        return self.saldo
