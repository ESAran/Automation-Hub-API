# 🧩 Etapa 3 — Autenticação com JWT

---

## 🎯 Objetivo

Implementar cadastro e autenticacao de usuarios, emitir tokens JWT e proteger as rotas de automacoes.

---

## 🧠 Competências trabalhadas

- Autenticacao e autorizacao em APIs REST
- Hash e verificacao segura de senhas
- Criacao e validacao de tokens JWT
- OAuth2 com Bearer Token no FastAPI
- Dependency injection para proteger endpoints
- Persistencia de usuarios com SQLAlchemy
- Evolucao do banco com Alembic

---

## 📚 O que estudar

### 1. Autenticação

- Diferenca entre autenticacao e autorizacao
- Credenciais, identidade e sessao stateless
- Fluxo de cadastro e login

### 2. Segurança de senhas

- Hash nao e criptografia
- Salt e algoritmos adaptativos
- Nunca armazenar ou retornar senha em texto puro

### 3. JWT

- Header, payload e signature
- Claims `sub`, `exp` e `iat`
- Assinatura, expiracao e validacao
- Bearer Token no cabecalho `Authorization`

### 4. FastAPI Security

- `OAuth2PasswordBearer`
- `OAuth2PasswordRequestForm`
- `Depends`
- Integracao com Swagger `/docs`

---

## 🛠️ Implementação

### 🔹 1. Instalar dependências

```bash
pip install PyJWT "pwdlib[argon2]" python-multipart
```

### 🔹 2. Configurar variáveis de ambiente

Adicionar ao `.env` e ao `.env.example`:

```env
JWT_SECRET_KEY=replace-with-a-secure-random-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

A chave real deve permanecer fora do Git.

### 🔹 3. Criar model User

Arquivo: `app/models/user.py`

Campos:

- `id`: Integer, primary key
- `email`: String, unique, indexed e non-nullable
- `hashed_password`: String e non-nullable
- `is_active`: Boolean e non-nullable

Regras:

- herdar de `Base`
- definir `__tablename__ = "users"`
- nunca armazenar senha em texto puro

### 🔹 4. Criar migration de usuários

Importar o model no `alembic/env.py` e executar:

```bash
alembic revision --autogenerate -m "create users table"
alembic upgrade head
```

Revisar a migration antes do upgrade.

### 🔹 5. Criar schemas de autenticação

Arquivo: `schemas/user.py`

Criar:

- `UserCreate`: email e password
- `UserResponse`: id, email e is_active
- `TokenResponse`: access_token e token_type

A senha deve existir apenas nos schemas de entrada.

### 🔹 6. Criar utilitários de segurança

Arquivo: `core/security.py`

Responsabilidades:

- gerar hash de senha
- verificar senha
- criar access token
- decodificar e validar JWT
- aplicar expiracao ao token

### 🔹 7. Criar service de usuários

Arquivo: `services/user_service.py`

Responsabilidades:

- buscar usuario por email
- rejeitar email duplicado
- cadastrar usuario com senha hasheada
- autenticar email e senha
- preservar regras de negocio fora das rotas

### 🔹 8. Criar rotas de autenticação

Arquivo: `api/routes/auth.py`

Endpoints:

- `POST /auth/register`: cadastrar usuario
- `POST /auth/token`: autenticar e retornar JWT
- `GET /auth/me`: retornar o usuario autenticado

O endpoint `/auth/token` deve usar `OAuth2PasswordRequestForm` para integrar o botao **Authorize** do Swagger.

### 🔹 9. Criar dependency de usuário autenticado

Arquivo: `api/dependencies/auth.py`

Implementar `get_current_user` para:

- receber o Bearer Token
- validar assinatura e expiracao
- extrair o usuario da claim `sub`
- consultar o usuario no banco
- responder `401 Unauthorized` quando invalido

### 🔹 10. Proteger rotas de automações

Aplicar `Depends(get_current_user)` nas rotas de automacoes.

Nesta etapa, autenticacao apenas exige um usuario valido. Propriedade de automacoes, permissoes e RBAC podem ser adicionados posteriormente.

### 🔹 11. Registrar router

Incluir o router de autenticacao no `main.py`.

---

## 🔄 Fluxo esperado

1. Usuario realiza cadastro
2. Senha e transformada em hash
3. Usuario realiza login
4. API valida as credenciais
5. API emite um JWT com expiracao
6. Cliente envia `Authorization: Bearer <token>`
7. Dependency valida o token e libera a rota protegida

---

## 🧪 Testes manuais

- cadastrar usuario valido
- rejeitar email duplicado
- confirmar que senha nao aparece nas respostas
- realizar login com credenciais validas
- rejeitar senha incorreta
- acessar `/auth/me` com token
- rejeitar token ausente, invalido ou expirado
- bloquear automacoes sem token
- liberar automacoes com token valido

---

## ✅ Critérios de conclusão

- usuarios persistidos por migration
- senhas armazenadas somente como hash
- login retorna access token JWT
- Swagger permite autenticacao pelo botao **Authorize**
- `/auth/me` retorna o usuario atual
- rotas de automacoes estao protegidas
- erros `400`, `401` e `409` estao documentados
- nenhuma chave ou credencial foi versionada

---

## ❌ O que evitar

- armazenar senha em texto puro
- incluir senha no JWT ou nas respostas
- deixar chave JWT fixa no codigo
- criar token sem expiracao
- acessar o banco diretamente nas rotas
- confiar no payload sem validar a assinatura

---

## 🎯 Resultado esperado

A API tera cadastro, login e identificacao do usuario por JWT, mantendo autenticacao stateless e rotas protegidas.

---

## 📍 Próxima etapa

Etapa 4 — Execução de automações
