# 🧩 Etapa 3 — Roteiro de Implementação (Autenticação com JWT)

---

## 🎯 Objetivo

Adicionar cadastro e autenticação de usuários à API utilizando:

- SQLAlchemy para persistência de usuários
- hash seguro de senhas com Argon2
- JWT para autenticação stateless
- OAuth2 Bearer Token no FastAPI
- dependency para proteção das rotas

---

## 🧠 Resultado esperado ao final

- Usuários cadastrados no banco de dados
- Senhas armazenadas somente como hash
- Login retornando access token JWT
- Endpoint para consultar o usuário autenticado
- Rotas de automações protegidas
- Autenticação disponível no Swagger
- Erros de autenticação tratados e documentados

---

# 🧱 PASSO 0 — Instalar dependências

Instalar:

```bash
pip install PyJWT "pwdlib[argon2]" python-multipart
```

Atualizar o arquivo `requirements.txt` após a instalação.

Responsabilidades das dependências:

- `PyJWT` → criar e validar tokens JWT
- `pwdlib[argon2]` → gerar e verificar hashes de senha
- `python-multipart` → receber o formulário OAuth2 de login

---

# 🧱 PASSO 1 — Criar estrutura de arquivos

Adicionar:

```text
app/
├── models/
│   └── user.py
api/
├── dependencies/
│   └── auth.py
└── routes/
	└── auth.py
core/
└── security.py
schemas/
└── user.py
services/
└── user_service.py
```

Atualizar também:

- `services/exceptions.py`
- `alembic/env.py`
- `api/routes/automations.py`
- `main.py`

---

# 🧱 PASSO 2 — Configurar variáveis de ambiente

Adicionar ao `.env`:

```env
JWT_SECRET_KEY=replace-with-a-secure-random-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Adicionar as mesmas chaves ao `.env.example`, sem incluir o segredo real.

Regras importantes:

- não versionar o `.env`
- não deixar o segredo JWT fixo no código
- validar se as configurações obrigatórias existem
- converter `ACCESS_TOKEN_EXPIRE_MINUTES` para inteiro

---

# 🧱 PASSO 3 — Criar model User

Arquivo: `app/models/user.py`

Criar classe `User` herdando de `Base`.

Definir:

- `__tablename__ = "users"`

Campos:

- `id` → Integer, primary key, autoincrement
- `email` → String, unique, indexed, non-nullable
- `hashed_password` → String, non-nullable
- `is_active` → Boolean, non-nullable, default `True`

Regras importantes:

- armazenar somente `hashed_password`
- nunca criar uma coluna `password`
- usar o email como identificador de login nesta etapa

---

# 🧱 PASSO 4 — Criar migration de usuários

No arquivo `alembic/env.py`:

- importar o model `User`
- manter `target_metadata = Base.metadata`

Gerar a migration:

```bash
alembic revision --autogenerate -m "create users table"
```

Revisar o arquivo gerado e validar:

- tabela `users`
- chave primária
- email único e indexado
- senha armazenada como `hashed_password`
- campo `is_active`
- `down_revision` apontando para a migration anterior

Aplicar:

```bash
alembic upgrade head
```

Validar:

- tabela `users` criada no banco
- `alembic_version` atualizada

---

# 🧱 PASSO 5 — Criar schemas de usuário

Arquivo: `schemas/user.py`

Criar `UserCreate`:

- `email` → email válido
- `password` → string com tamanho mínimo e máximo definidos

Criar `UserResponse`:

- `id`
- `email`
- `is_active`
- habilitar leitura de atributos ORM com `from_attributes=True`

Criar `TokenResponse`:

- `access_token`
- `token_type`

Regras importantes:

- senha deve existir somente no schema de entrada
- `hashed_password` nunca deve aparecer nas respostas
- separar schemas de entrada e saída

---

# 🧱 PASSO 6 — Criar exceções de autenticação

Arquivo: `services/exceptions.py`

Adicionar exceções de domínio para:

- email já cadastrado
- credenciais inválidas
- usuário inativo

Responsabilidade:

- service levanta exceções de domínio
- rota converte exceções em respostas HTTP

Status esperados:

- email duplicado → `409 Conflict`
- credenciais inválidas → `401 Unauthorized`
- usuário inativo → `403 Forbidden`

---

# 🧱 PASSO 7 — Criar utilitários de segurança

Arquivo: `core/security.py`

Configurar o gerenciador de senhas com Argon2.

Implementar:

---

`hash_password(password)`

- receber senha em texto puro
- gerar hash seguro
- retornar somente o hash

---

`verify_password(password, hashed_password)`

- comparar senha informada com o hash salvo
- retornar verdadeiro ou falso

---

`create_access_token(subject)`

- usar o ID do usuário como claim `sub`
- adicionar `iat`
- adicionar `exp`
- assinar com `JWT_SECRET_KEY`
- usar o algoritmo configurado

---

`decode_access_token(token)`

- validar assinatura
- validar expiração
- extrair a claim `sub`
- rejeitar token inválido

Regras importantes:

- nunca incluir senha ou hash no token
- sempre definir expiração
- nunca confiar no payload sem validar a assinatura

---

# 🧱 PASSO 8 — Criar Service Layer de usuários

Arquivo: `services/user_service.py`

O service deve receber `db: Session` e não depender do FastAPI.

Implementar:

---

`get_user_by_email(db, email)`

- consultar usuário pelo email
- retornar usuário ou `None`

---

`get_user_by_id(db, user_id)`

- consultar usuário pelo ID
- retornar usuário ou `None`

---

`create_user(db, data)`

- verificar se o email já existe
- gerar hash da senha
- criar objeto ORM `User`
- adicionar na session
- executar commit
- executar refresh
- retornar usuário criado

---

`authenticate_user(db, email, password)`

- buscar usuário pelo email
- verificar senha
- verificar se o usuário está ativo
- retornar usuário autenticado
- levantar erro para credenciais inválidas

Regras importantes:

- não retornar senha ou hash
- não colocar `HTTPException` no service
- manter regras de negócio fora das rotas

---

# 🧱 PASSO 9 — Criar dependency de autenticação

Arquivo: `api/dependencies/auth.py`

Configurar:

```text
OAuth2PasswordBearer(tokenUrl="/auth/token")
```

Implementar `get_current_user`:

- receber token da dependency OAuth2
- decodificar e validar o JWT
- extrair o ID da claim `sub`
- buscar usuário no banco
- validar se o usuário existe e está ativo
- retornar o objeto ORM `User`

Responder `401 Unauthorized` quando:

- token estiver ausente
- assinatura for inválida
- token estiver expirado
- claim `sub` estiver ausente ou inválida
- usuário não existir

Incluir o cabeçalho:

```text
WWW-Authenticate: Bearer
```

---

# 🧱 PASSO 10 — Criar rotas de autenticação

Arquivo: `api/routes/auth.py`

Criar router:

```text
prefix="/auth"
tags=["Authentication"]
```

---

`POST /auth/register`

- receber `UserCreate`
- chamar `create_user`
- retornar `UserResponse`
- status `201 Created`
- tratar email duplicado com `409 Conflict`

---

`POST /auth/token`

- receber `OAuth2PasswordRequestForm`
- interpretar `username` como email
- chamar `authenticate_user`
- criar access token
- retornar `TokenResponse`
- tratar credenciais inválidas com `401 Unauthorized`

---

`GET /auth/me`

- usar `Depends(get_current_user)`
- retornar `UserResponse`
- não consultar senha ou expor o hash

Regras importantes:

- documentar summaries, descriptions e responses no Swagger
- não acessar o banco diretamente nas rotas
- repassar a session para o service

---

# 🧱 PASSO 11 — Registrar router no main

Arquivo: `main.py`

Importar o router de autenticação e registrar:

```text
app.include_router(auth_router)
```

Validar no Swagger:

- seção `Authentication`
- endpoint de cadastro
- endpoint de token
- endpoint `/auth/me`
- botão **Authorize** disponível

---

# 🧱 PASSO 12 — Proteger rotas de automações

Arquivo: `api/routes/automations.py`

Adicionar a dependency `get_current_user` às rotas de automações.

Nesta etapa, a regra será:

- qualquer usuário autenticado pode acessar o CRUD de automações
- requisições sem token devem receber `401 Unauthorized`
- token válido libera o acesso

Fora do escopo desta etapa:

- associar automação ao usuário proprietário
- permissões por função
- RBAC

---

# 🧪 PASSO 13 — Teste manual

Rodar:

```bash
uvicorn main:app --reload
```

Abrir:

```text
http://127.0.0.1:8000/docs
```

Testar cadastro:

- criar usuário válido
- tentar cadastrar o mesmo email novamente
- confirmar que senha e hash não aparecem na resposta

Testar login:

- autenticar com email e senha válidos
- verificar `access_token`
- verificar `token_type = "bearer"`
- tentar senha incorreta
- tentar email inexistente

Testar usuário atual:

- autorizar no Swagger com token válido
- acessar `GET /auth/me`
- validar os dados retornados

Testar proteção:

- acessar automações sem token
- acessar automações com token inválido
- acessar automações com token válido
- testar token expirado

---

# ✅ CHECKLIST FINAL

- dependências instaladas
- variáveis JWT configuradas
- `.env` fora do Git
- model `User` criado
- migration criada, revisada e aplicada
- senha armazenada somente como hash
- schemas de entrada e saída separados
- cadastro funcionando
- email duplicado tratado
- login retornando JWT
- token com assinatura e expiração
- `/auth/me` funcionando
- botão **Authorize** funcionando no Swagger
- rotas de automações protegidas
- erros `401`, `403` e `409` tratados
- API funcionando sem regressão no CRUD

---

# ❌ O que NÃO fazer

- armazenar senha em texto puro
- retornar senha ou hash na API
- colocar segredo JWT no código
- versionar o `.env`
- criar token sem expiração
- incluir informações sensíveis no JWT
- acessar banco diretamente nas rotas
- usar `HTTPException` dentro do service
- confiar em token sem validar assinatura

---

# 🚀 Diferenciais (opcional)

- adicionar refresh token
- permitir revogação de tokens
- implementar recuperação de senha
- confirmar email do usuário
- adicionar rate limiting no login
- criar permissões e RBAC
- associar automações ao usuário proprietário

---

# 🎯 Resultado final

Você terá:

- usuários persistidos no banco
- senhas protegidas com hash seguro
- autenticação stateless com JWT
- integração OAuth2 com o Swagger
- rotas protegidas por dependency
- base para autorização e permissões futuras

---

# 📍 Próximo passo

Etapa 4 — Execução de automações. 
