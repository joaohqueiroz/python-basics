from conta import Conta


class ContaCorrente(Conta):

    def __init__(self, agencia: int, numero: int, saldo: float = 0, limite: float = 0) -> None:
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor) -> float:
        novo_valor = self.saldo - valor

        if novo_valor >= -self.limite:
            self.saldo = novo_valor
            self.detalhes(f'Saque: R${valor:.2f}')
            return self.saldo

        print(f'Não é possível sacar o valor desejado. Seu saldo atual é: R${self.saldo}')
        print(f'Seu limite é: R${self.limite}')
        return self.saldo
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.agencia!r}, {self.numero!r}, {self.saldo!r}, {self.limite!r})'
