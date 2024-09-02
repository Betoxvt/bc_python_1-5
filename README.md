# Aulas e desafios do bootcamp python 1-5
## Aula01
1. Instalação de python vscode git e github
2. Mais uma coisas básicas sobre os citados acima
3. Um desafio para iniciar os exercícios
## Aula02
1. Lista de exercícios 01 ao 25
2. Erros:
    - procurar na documentação em inglês;
    - pensar em todos os testes e erros pode levar 2x mais tempo do que fazer o código;
    - tipos de erros;
    - try, except, else, finally, if isinstance(numero, int);
    - use os try e except para diferenciar seu código
3. Desafio com tratamento de erros
## Aula03
1. Controle de fluxo
* Precisamos definir uma rota de como a aplicação deve funcionar;
* Airflow > Ferramenta de orquestração;
* if elif else... testes em ordem, o que for, será executado;

2. Debug
* Faz linha por linha devagar para testar o script/código;
* No VSCode você pode adicionar os pontos de parada, na esquerda do código ou simplesmente mandar fazer linha por linha;
* Tem uma janela que mostra as variáveis sendo atribuidas (locais e globais);
* Permite ver o fluxo e a organização do programa;

3. Listas e dicionários

4. Desafio com loop de validação
## Aula04 
1. Tipos complexos
* Tuplas
* Listas: `lista.extend(range())`
* Dicionários se comunica com json do JS. `json.dump(coisa)`, `import typing`

2. Type Hint (Dicionários vs Data frames vs Tabelas vs Excel)
* No Python não precisa 'tipar', ele faz por inferência... entende qual é o tipo da variável.
* O Type hint é uma dica que serve para quem for ler o código e entender o que estava na mente de quem escreveu. `var`: `type` = `data`. Mas não faz mais nada, só uma dica mesmo para os desenvolvedores.
* Exemplos:
    - idade: int = 30
    - altura: float = 1.75
    - nome: str = "Alice"
    - is_estudante: bool = True
* Tipagem forte: não permite alterar tipos de variáveis em tempo de execução. Oposto da tipagem fraca ('11' + 1 = 111)
* Tipagem dinâmica: permite que o interpretador infira o tipo da variável durante a execução. Oposto da tipagem estática.

3. Lendo Arquivo
* ETL : Extract - Transform - Load
* `import csv` ou pandas
* `with` gerenciador de contexto. ele abre a fecha o arquivo. útil pra não esquecer de fechar e dar ruim.

4. Definir função
def isso(n: list) -> list:
* PEP: nome_bem_completo, tipar as coisas
* Pydantic é fod# no controle, dar uma olhada nisso
