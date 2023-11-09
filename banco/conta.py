from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0) -> None:
        super().__init__()
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Depósito: R${valor:.2f}')
        return self.saldo

    def detalhes(self, msg=''):
        print(f'O seu saldo é R${self.saldo:.2f}. {msg}')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.agencia!r}, {self.numero!r}, {self.saldo!r})'
