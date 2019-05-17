# Mini Redis

Solução proposta por Lucas Gonçalves Bonilla para seleção de programador BackEnd

A solução proposta implementa algumas funções de uma base de dados NoSQL REDIS.
São elas:
- SET
- GET
- DEL
- DBSIZE
- INCR
- ZADD
- ZCARD
- ZRANK
- ZRANGE

A Linguagem utilizada foi Python na sua versão 3.7 juntamente com o framework Flask para implementar as requisições HTTP solicitadas ao fim do desafio. A escolha da linguagem e do framework se deram pela familiaridade com as ferramentas.

Para utilizar a solução proposta deve ser criado um ambiente virtual com virtualenv.
Para criar o ambiente virutal rode o comando:
```sh
> virtualenv venv
```
Agora ative o ambiente virtual com:
```sh
> source vevn/bin/activate
```
Em seguida, para instalar as dependências, rode:
```sh
> pip install -r requirements.txt
```

Para testar o sistema pode ser rodado o arquivo de testes unitários com o comando:
```sh
> python -m unittest
> python -m unittest discover -v
```

Se houver instalada na sua IDE um simulador de requisições REST pode ser testado também através do arquivo tests/.rest

Cronograma:

| Tarefas | 10/05 | 11/05 | 12/05 | 13/05 | 14/05 | 15/05 |16/05|17/05|
| - | - | - | - | - | - | - | - | - |
| Conhecer REDIS | * | * |  |  |  |  |  |  |
| Traçar estratégias | * | * | * |  |  |  |  |  |
| Estudar comandos REDIS | * | * | * | * |  |  |  |  |
| Implementar comandos REDIS | * | * | * | * | * |  |  |  |
| Refatorar códigos |  |  |  |  | * | * | * | * |
| Testar métodos |  |  |  |  | * | * | * | * |
| Testes Unitários |  |  |  |  |  |  | * | * |
| Escrever READ.me |  |  |  |  |  |  |  | * |

Tempo aplicado 

| Dia | > 2hs | 2hs - 3hs | 3hs-4hs | < 4hs |
| - | - | - | - | - |
|10/05|  |  |  | * |
|11/05 |  |  |  | * |
|12/05 | * |  |  |  |
|13/05 |  | * |  |  |
|14/05 |  | * |  |  |
|15/05 | * |  |  |  |
|16/05|  |  |  |  |
|17/05|  |  |  | * |
