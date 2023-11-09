from pessoa_package.pessoa import Pessoa
import json

with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    p1 = Pessoa(**json.load(arquivo))
    print(vars(p1))