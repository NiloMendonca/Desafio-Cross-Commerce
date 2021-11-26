# Desafio Cross Commerce
Projeto com o objetivo de desenvolver o desafio Cross Commerce.

## Ambiente de desenvolvimento

Clone o repositório.

### pip

Atualize a lista das versões dos pacotes disponíveis.

```
sudo apt update
```

Instale o pip.
```
sudo apt install python3-pip
```

Atualize o pip.
```
pip3 install --upgrade pip
```

### Virtualenv

Instale o Virtualenv.

```
pip3 install virtualenv
```

Crie um ambiente virtual.

```
virtualenv env
```

Ative o ambiente.
```
source env/bin/activate
```

### Requisitos

Instale os requisitos.
```
pip3 install -r requirements.txt
```

### Execução

```
python3 run.py
```

### Funcionamento

#### Visualização pelo navegador

- Todos os números ordenados:
Para visualizar todos os números ordenados pelo navegador acesse "http://127.0.0.1:5000".

- Números ordenados por página:
Para visualizar os números ordenados por páginas pelo navegador acesse "http://127.0.0.1:5000?page=1" (substituir o valor "1" pelo número da página desejada, caso a página seja maior que a quantidade de números disponibilizados será exibido um vetor vazio "[]").

#### API

- Todos os números ordenados:
Para retornar todos os números ordenados realize um Get para "http://127.0.0.1:5000/numbers".

- Números ordenados por página:
Para retornar os números ordenados por páginas realize um Get para "http://127.0.0.1:5000/numbers?page=1" (substituir o valor "1" pelo número da página desejada, caso a página seja maior que a quantidade de números disponibilizados será retornado um vetor vazio "[]").


### Testes

Os testes da aplicação estão disponíveis no diretório "test". Passos para sua execução:

Entre no diretório:
```
cd test
```

Execute o arquivo de testes:
```
pytest default.py
```