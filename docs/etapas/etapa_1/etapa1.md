# 🧩 Etapa 1 — Setup + Primeira API

---

## 🎯 Objetivo

Construir uma API funcional, organizada e com padrão de mercado utilizando FastAPI, sem uso de banco de dados (persistência em memória).

---

## 🧠 Competências trabalhadas

- Fundamentos de API REST
- Estruturação de projeto backend
- Uso de FastAPI
- Validação com Pydantic
- Separação de responsabilidades (routes, services, schemas)

---

## 📚 O que estudar

### 1. HTTP + REST
- Métodos: GET, POST, PUT, DELETE
- Status codes:
  - 200 (OK)
  - 201 (Created)
  - 400 (Bad Request)
  - 404 (Not Found)
- Conceito de recursos (`/automations`)

---

### 2. FastAPI
- Criação de rotas
- Request body
- Response model
- Documentação automática (Swagger)

---

### 3. Pydantic
- Criação de schemas
- Validação de dados
- Tipagem

---

### 4. Estrutura de projeto
- Separação em camadas:
  - routes
  - services
  - schemas

---

## 🛠️ Implementação

### 🔹 1. Setup do ambiente

python -m venv venv  
source venv/bin/activate  (Mac/Linux)  
venv\Scripts\activate     (Windows)  

pip install fastapi uvicorn  

---

### 🔹 2. Estrutura inicial

app/  
├── main.py  
├── api/  
│   └── routes/  
│       └── automations.py  
├── schemas/  
│   └── automation.py  
├── services/  
│   └── automation_service.py  

---

### 🔹 3. Criar aplicação principal

- Instanciar FastAPI  
- Registrar rotas  

---

### 🔹 4. Endpoint de saúde

GET /health  

Resposta esperada:

{
  "status": "ok"
}

---

### 🔹 5. CRUD de automations (em memória)

Estrutura do objeto:

{
  "id": 1,
  "name": "Importar dados",
  "description": "Script que puxa dados da API X",
  "is_active": true
}

---

### 🔹 Endpoints obrigatórios

Criar automação  
POST /automations  

Listar automações  
GET /automations  

Buscar por ID  
GET /automations/{id}  

Atualizar  
PUT /automations/{id}  

Deletar  
DELETE /automations/{id}  

---

### 🔹 6. Service Layer

Arquivo:  
services/automation_service.py  

Responsável por:  
- Lógica de CRUD  
- Armazenamento em memória  
- Separação da lógica das rotas  

---

### 🔹 7. Schemas (Pydantic)

Criar:

- AutomationCreate  
- AutomationUpdate  
- AutomationResponse  

---

## 🔄 Fluxo de desenvolvimento

1. Criar schemas  
2. Criar service  
3. Criar rotas  
4. Conectar no main  

---

## ✅ Critérios de conclusão

- API rodando com uvicorn  
- Swagger disponível (/docs)  
- CRUD completo funcionando  
- Código organizado em camadas  
- Uso correto de Pydantic  

---

## ❌ O que evitar

- Colocar tudo no main.py  
- Misturar lógica com rotas  
- Não usar schemas  
- Não tratar erro (ID inexistente)  

---

## 🚀 Diferenciais (opcional)

- Usar UUID ao invés de int  
- Validação de campos obrigatórios  
- Tipagem completa  
- Responses padronizadas  

---

## 🎯 Resultado esperado

Você será capaz de:

- Criar uma API REST funcional  
- Estruturar backend como mercado exige  
- Trabalhar com FastAPI de forma profissional  

---

## 📍 Próxima etapa

Etapa 2 — Banco de Dados  