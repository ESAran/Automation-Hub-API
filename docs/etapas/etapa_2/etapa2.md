# 🧩 Etapa 2 — Banco de Dados (PostgreSQL + ORM)

---

## 🎯 Objetivo

Substituir a persistência em memória por um banco de dados real, utilizando PostgreSQL e ORM.

---

## 🧠 Competências trabalhadas

- Integração com banco de dados relacional
- Modelagem de dados
- Uso de ORM (SQLAlchemy)
- Migrations com Alembic
- Separação entre domínio e persistência

---

## 📚 O que estudar

### 1. SQL (básico aplicado)
- SELECT
- INSERT
- UPDATE
- DELETE
- WHERE
- PRIMARY KEY

---

### 2. SQLAlchemy
- Engine
- Session
- Models
- CRUD com ORM

---

### 3. Alembic
- Migrations
- Versionamento de schema
- upgrade / downgrade

---

### 4. PostgreSQL
- Conexão
- Banco local
- Estrutura básica

---

## 🛠️ Implementação

---

### 🔹 1. Instalar dependências

pip install sqlalchemy psycopg2-binary alembic  

---

### 🔹 2. Criar banco de dados

Criar banco local:

automation_hub  

---

### 🔹 3. Criar estrutura de banco

Adicionar nova pasta:

app/db/  
├── session.py  
├── base.py  

---

### 🔹 4. Criar conexão com banco

Arquivo: db/session.py  

Responsável por:

- Criar engine  
- Criar SessionLocal  
- Gerenciar conexão  

---

### 🔹 5. Criar base do ORM

Arquivo: db/base.py  

Responsável por:

- Declarative Base  

---

### 🔹 6. Criar models (substitui dict)

Criar pasta:

app/models/  

Criar arquivo:

automation.py  

---

### Model Automation

Campos:

- id (int, primary key)
- name (string)
- description (string)
- is_active (boolean)

---

### 🔹 7. Configurar Alembic

Rodar:

alembic init alembic  

---

Configurar:

- URL do banco
- Importar Base

---

### 🔹 8. Criar primeira migration

alembic revision --autogenerate -m "create automations table"  

---

Aplicar:

alembic upgrade head  

---

### 🔹 9. Refatorar Service Layer

Substituir:

- lista em memória ❌  
- por acesso ao banco ✔  

---

Atualizar funções:

- create → insert no banco  
- list → select  
- get → query por id  
- update → update  
- delete → delete  

---

### 🔹 10. Usar session no service

- Abrir sessão  
- Executar operação  
- Commit  
- Fechar sessão  

---

## 🔄 Fluxo de desenvolvimento

1. Criar conexão  
2. Criar models  
3. Configurar migration  
4. Criar tabela  
5. Refatorar service  

---

## ✅ Critérios de conclusão

- Banco criado  
- Tabela criada via migration  
- CRUD funcionando com banco  
- Sem uso de lista em memória  
- API continua funcionando  

---

## ❌ O que evitar

- Misturar lógica de banco nas rotas  
- Acessar banco direto no controller  
- Não usar migration  
- Hardcode de conexão  

---

## 🚀 Diferenciais (opcional)

- Usar UUID como ID  
- Criar BaseModel separado para ORM  
- Separar config em arquivo  
- Criar dependency de DB session no FastAPI  

---

## 🎯 Resultado esperado

Você será capaz de:

- Trabalhar com banco real  
- Usar ORM profissionalmente  
- Criar migrations  
- Persistir dados corretamente  

---

## 📍 Próxima etapa

Etapa 3 — Autenticação (JWT)