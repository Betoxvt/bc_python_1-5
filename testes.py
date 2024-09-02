name: str = 'Valindra'
age: int = 438
monster_type: str = 'Lich'
monster_subType: str = 'Elf'
monster_class: str = 'Mage'

valindra: dict = {'Nome': name, 'Classe': monster_class, 'Idade': age, 'Raça': monster_type, 'Sub-raça': monster_subType}

for k, v in valindra.items():
    print(f'{k}: {v}')

lista_keys = [x for x in valindra.keys()]
print(lista_keys)
lista_values = [x for x in valindra.values()]
print(lista_values)

novo_dict = {x: v for x, v in zip(lista_keys, lista_values)}
print(novo_dict)