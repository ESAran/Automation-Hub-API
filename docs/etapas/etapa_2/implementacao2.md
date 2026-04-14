# 🧩 Etapa 2 — Roteiro de Implementação (Banco de Dados)

---

## 🎯 Objetivo

Substituir a persistência em memória por banco de dados real utilizando PostgreSQL + SQLAlchemy + Alembic.

---

## 🧠 Resultado esperado ao final

- Banco de dados funcionando
- Tabela criada via migration
- CRUD funcionando com banco
- Service usando ORM
- Nenhum uso de lista em memória

---

# 🧱 PASSO 0 — Instalar dependências

pip install sqlalchemy psycopg2-binary alembic  

---

# 🧱 PASSO 1 — Criar banco de dados

Criar banco local (exemplo):

automation_hub  

---

# 🧱 PASSO 2 — Criar estrutura de pastas

Adicionar:

app/  
├── db/  
│   ├── session.py  
│   └── base.py  
├── models/  
│   └── automation.py  

---

# 🧱 PASSO 3 — Configurar conexão com banco

Arquivo: app/db/session.py  

Responsabilidades:

- Criar engine  
- Criar SessionLocal  
- Conectar com PostgreSQL  

---

Implementar:

- string de conexão  
- engine  
- sessionmaker  

---

# 🧱 PASSO 4 — Criar Base do ORM

Arquivo: app/db/base.py  

Responsabilidade:

- Criar Base do SQLAlchemy  

---

Implementar:

Base = declarative_base()  

---

# 🧱 PASSO 5 — Criar model Automation

Arquivo: app/models/automation.py  

---

Criar classe Automation

Campos:

- id → Integer, primary key  
- name → String  
- description → String  
- is_active → Boolean  

---

Regras:

- usar Base  
- definir __tablename__  

---

# 🧱 PASSO 6 — Configurar Alembic

Rodar:

alembic init alembic  

---

Configurar:

- alembic.ini → URL do banco  
- env.py → importar Base  

---

# 🧱 PASSO 7 — Criar migration

Rodar:

alembic revision --autogenerate -m "create automations table"  

---

Aplicar:

alembic upgrade head  

---

Validar:

- tabela criada no banco  

---

# 🧱 PASSO 8 — Refatorar Service Layer

Arquivo: services/automation_service.py  

---

REMOVER:

- lista em memória  
- next_id  

---

ADICIONAR:

- uso de session do banco  

---

Atualizar funções:

---

create_automation

- criar objeto ORM  
- adicionar na session  
- commit  
- refresh  
- retornar  

---

list_automations

- query all  

---

get_automation_by_id

- query por id  
- tratar erro  

---

update_automation

- atualizar campos  
- commit  

---

delete_automation

- deletar  
- commit  

---

# 🧱 PASSO 9 — Gerenciar sessão

Você deve:

- abrir session  
- usar session  
- fechar session  

---

(na etapa seguinte você melhora isso com dependency)

---

# 🧪 PASSO 10 — Teste manual

Rodar:

uvicorn app.main:app --reload  

---

Testar no /docs:

- criar automation  
- listar  
- buscar  
- atualizar  
- deletar  

---

# ✅ CHECKLIST FINAL

- banco criado  
- tabela criada via migration  
- CRUD funcionando com banco  
- sem uso de lista em memória  
- service usando ORM  
- API funcionando igual antes  

---

# ❌ O que NÃO fazer

- acessar banco direto na rota  
- misturar lógica com controller  
- não usar migration  
- deixar código acoplado  

---

# 🚀 Diferenciais (opcional)

- usar UUID como ID  
- criar config.py para conexão  
- criar dependency de DB session  
- separar camada repository  

---

# 🎯 Resultado final

Você terá:

- backend com banco real  
- uso de ORM profissional  
- migrations funcionando  
- base para sistemas reais  

---

# 📍 Próximo passo

Etapa 3 — Autenticação (JWT)