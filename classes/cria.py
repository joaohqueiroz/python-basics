from pessoa_package.pessoa import Pessoa
import json

p1 = Pessoa("João", "Queiroz", 2000)

with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(vars(p1), arquivo)