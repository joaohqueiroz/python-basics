from pessoa import Pessoa
from conta import Conta


class Banco:

    def __init__(self, agencias: list[int] | None = None, clientes: list[Pessoa] | None = None, contas: list[Conta] | None = None):
        