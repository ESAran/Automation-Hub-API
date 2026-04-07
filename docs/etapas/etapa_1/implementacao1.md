# 🧩 Etapa 1 — Roteiro de Implementação (Setup + Primeira API)

---

## 🎯 Objetivo

Construir uma API REST funcional com FastAPI, seguindo padrão de mercado:

- Estrutura organizada (routes, schemas, services)
- CRUD completo de automations
- Persistência em memória (sem banco)
- Código limpo e separado por responsabilidade

---

## 🧠 Resultado esperado ao final

- API rodando em /docs
- CRUD completo funcional
- Estrutura de projeto profissional
- Separação correta de camadas
- Tratamento básico de erros

---

# 🧱 PASSO 0 — Setup do projeto

Criar projeto:

mkdir automation-hub  
cd automation-hub  
python -m venv venv  

---

Ativar ambiente:

Mac/Linux:  
source venv/bin/activate  

Windows:  
venv\Scripts\activate  

---

Instalar dependências:

pip install fastapi uvicorn  

---

# 🧱 PASSO 1 — Estrutura de pastas

Criar estrutura:

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

# 🧱 PASSO 2 — Criar aplicação principal

Arquivo: app/main.py  

Responsabilidades:

- Criar instância do FastAPI  
- Criar endpoint /health  
- Registrar rotas  

---

Implementar:

Criar app:  
app = FastAPI()  

Criar rota:  
@app.get("/health")  
def health():  
    return {"status": "ok"}  

---

Rodar servidor:

uvicorn app.main:app --reload  

---

Validar:

- Acessar: http://127.0.0.1:8000/docs  
- Testar endpoint /health  

---

# 🧱 PASSO 3 — Criar schemas (Pydantic)

Arquivo: schemas/automation.py  

---

AutomationCreate (entrada):

- name: str  
- description: str  
- is_active: bool  

---

AutomationUpdate (entrada parcial):

- name: opcional  
- description: opcional  
- is_active: opcional  

---

AutomationResponse (saída):

- id: int  
- name: str  
- description: str  
- is_active: bool  

---

Regras importantes:

- Não reutilizar schema de create como response  
- Separar claramente entrada e saída  
- Usar tipagem correta  

---

# 🧱 PASSO 4 — Criar Service Layer

Arquivo: services/automation_service.py  

---

Responsabilidade:

- Centralizar toda lógica  
- Simular banco de dados em memória  
- Não depender do FastAPI  

---

Estrutura base:

- lista de automations  
- contador de ID  

Exemplo lógico:

automations = []  
next_id = 1  

---

Funções obrigatórias:

---

create_automation(data)

- gerar ID  
- criar objeto  
- salvar na lista  
- retornar objeto  

---

list_automations()

- retornar todas  

---

get_automation_by_id(id)

- buscar automation  
- se não existir → erro  

---

update_automation(id, data)

- buscar automation  
- atualizar apenas campos enviados  
- retornar atualizado  

---

delete_automation(id)

- buscar automation  
- remover da lista  

---

Regras importantes:

- Não usar FastAPI aqui  
- Não usar request/response  
- Service deve ser independente  

---

# 🧱 PASSO 5 — Criar rotas

Arquivo: api/routes/automations.py  

---

Criar router:

router = APIRouter(prefix="/automations", tags=["Automations"])  

---

Endpoints:

---

POST /automations

- recebe AutomationCreate  
- retorna AutomationResponse  
- status 201  

---

GET /automations

- retorna lista  

---

GET /automations/{id}

- retorna automation específica  

---

PUT /automations/{id}

- atualiza automation  

---

DELETE /automations/{id}

- remove automation  

---

Regras importantes:

- usar response_model  
- não colocar lógica nas rotas  
- sempre chamar service  

---

# 🧱 PASSO 6 — Conectar rotas no main

No main.py:

app.include_router(router)  

---

# 🧱 PASSO 7 — Tratamento de erros

Tratar:

- ID não encontrado  

Usar:

HTTPException(status_code=404, detail="Automation not found")  

---

# 🧪 PASSO 8 — Teste manual

Abrir:

http://127.0.0.1:8000/docs  

---

Testar fluxo completo:

- criar automation  
- listar  
- buscar por ID  
- atualizar  
- deletar  

---

# ✅ CHECKLIST FINAL

- API rodando  
- Swagger funcionando  
- CRUD completo  
- Estrutura organizada  
- Service separado  
- Schemas corretos  
- Erros tratados  

---

# ❌ O que NÃO fazer

- Colocar tudo no main.py  
- Misturar lógica com rota  
- Não usar schemas  
- Não tratar erro  
- Código desorganizado  

---

# 🚀 Diferenciais (opcional)

- usar UUID ao invés de int  
- validação de campos  
- tipagem completa  
- separar ainda mais responsabilidades  

---

# 🎯 Resultado final

Você terá:

- primeira API estruturada corretamente  
- base sólida de backend  
- padrão de projeto de mercado  

---

# 📍 Próximo passo

Etapa 2 — Banco de Dados  