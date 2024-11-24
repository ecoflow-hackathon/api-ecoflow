# **Cadeia de Produção de Cacau - API**

Esta API gerencia informações sobre a cadeia de produção de cacau, permitindo que produtores registrem dados relacionados a lotes e visualizem essas informações via QR Code.

## **Estrutura do Projeto**
- **Produtores**: Representam os participantes da cadeia de produção.
- **Lotes**: Identificam os lotes de produção de cacau.
- **Informações de Produção**: Detalhes como o consumo de água e emissões de carbono associados a cada lote.

---

## **Instalação**
1. Clone o repositório:
   ```bash
   git clone https://github.com/ecoflow-hackathon/api-ecoflow.git
   cd api-ecoflow

2. Crie um ambiente virtual:
   ```bash
   python -m venv venvsource venv/bin/activate  # No Windows, use venv\Scripts\activate

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Realize as migrações para configurar o banco de dados:
    ```bash
    python manage.py migrate

5. Crie um superusuário para acessar o painel administrativo:
    ```bash
    python manage.py createsuperuser

6. Inicie o servidor:
    ```bash
    python manage.py runserver


# Endpoints da API
## 1. Produtores
POST /api/produtores/
Cria um novo produtor.

Exemplo de Requisição:
```
{
  "nome": "João da Silva",
  "email": "joao@email.com",
  "telefone": "123456789"
}
```
Resposta: 
```
{
  "id": 1,
  "nome": "João da Silva",
  "email": "joao@email.com",
  "telefone": "123456789"
}
```

GET /api/produtores/
Lista todos os produtores.

Resposta:
```
[
  {
    "id": 1,
    "nome": "João da Silva",
    "email": "joao@email.com",
    "telefone": "123456789"
  },
  {
    "id": 2,
    "nome": "Maria Oliveira",
    "email": "maria@email.com",
    "telefone": "987654321"
  }
]
```
## 2. Lotes
POST /api/lotes/
Cria um novo lote.

Exemplo de Requisição:
```
{
  "identificador": "Lote001",
  "produtores": [1, 2]
}

```
Resposta:
```
{
  "id": 1,
  "identificador": "Lote001",
  "produtores": [
    {
      "id": 1,
      "nome": "João da Silva"
    },
    {
      "id": 2,
      "nome": "Maria Oliveira"
    }
  ]
}
```
GET /api/lotes/
Lista todos os lotes.

Resposta:
```
[
  {
    "id": 1,
    "identificador": "Lote001",
    "produtores": [
      {
        "id": 1,
        "nome": "João da Silva"
      },
      {
        "id": 2,
        "nome": "Maria Oliveira"
      }
    ]
  }
]
```
## 3. Informações de Produção
POST /api/informacoes/
Cria uma nova informação de produção para um lote.

Exemplo de Requisição:
```
{
  "lote": 1,
  "produtor": 1,
  "descricao": "Consumo de água e emissões",
  "quantidade_agua": 150.5,
  "emissao_carbono": 25.3
}
```
Resposta:
```
{
  "id": 1,
  "lote": 1,
  "produtor": {
    "id": 1,
    "nome": "João da Silva"
  },
  "descricao": "Consumo de água e emissões",
  "quantidade_agua": 150.5,
  "emissao_carbono": 25.3
}
```
GET /api/informacoes/
Lista todas as informações de produção.

Resposta:
```
[
  {
    "id": 1,
    "lote": 1,
    "produtor": {
      "id": 1,
      "nome": "João da Silva"
    },
    "descricao": "Consumo de água e emissões",
    "quantidade_agua": 150.5,
    "emissao_carbono": 25.3
  }
]
```
PUT /api/informacoes/{id}/
Atualiza uma informação de produção.

Exemplo de Requisição:
```
{
  "descricao": "Consumo atualizado",
  "quantidade_agua": 170.0,
  "emissao_carbono": 30.0
}
```
Resposta:
```
{
  "id": 1,
  "lote": 1,
  "produtor": {
    "id": 1,
    "nome": "João da Silva"
  },
  "descricao": "Consumo atualizado",
  "quantidade_agua": 170.0,
  "emissao_carbono": 30.0
}
```
