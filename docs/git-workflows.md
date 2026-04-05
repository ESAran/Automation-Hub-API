# 🌿 Git Workflow — Automation Hub API

---

## 🎯 Objetivo

Utilizar Git de forma profissional, simulando ambiente real de desenvolvimento em equipe.

---

## 🧠 Princípios

- Cada funcionalidade = uma branch
- Nunca desenvolver diretamente na `main`
- Commits pequenos, claros e frequentes
- Histórico limpo e fácil de entender

---

## 🌳 Estrutura de Branches

### 🔹 main
- Código estável
- Sempre funcional
- Pronto para produção

---

### 🔹 develop (recomendado)
- Integração de features
- Onde as branches são unidas

---

### 🔹 feature branches

Padrão:

feature/nome-da-feature

Exemplos:

feature/project-setup  
feature/health-check  
feature/automation-schemas  
feature/automation-service  
feature/automation-routes  

---

## 🔄 Fluxo de Trabalho

### 1. Criar branch

git checkout -b feature/nome-da-feature

---

### 2. Desenvolver a funcionalidade

- Escrever código
- Testar localmente
- Validar funcionamento

---

### 3. Fazer commits

Padrão de mensagem:

tipo: descrição curta

---

## 🧾 Tipos de Commit

- feat → nova funcionalidade  
- fix → correção de bug  
- refactor → melhoria de código  
- chore → ajustes gerais  
- docs → documentação  

---

## ✍️ Exemplos de Commits

feat: add health check endpoint  
feat: implement automation CRUD  
feat: create automation schemas  
feat: add automation service layer  

fix: handle automation not found error  

refactor: move logic to service layer  

---

## 📌 Regras de Commit

- Um commit = uma mudança lógica
- Evitar commits grandes demais
- Evitar mensagens vagas:
  - ❌ "ajustes"
  - ❌ "update"
  - ❌ "mudanças"

---

## 🔼 Subir código

git add .  
git commit -m "feat: descrição"  
git push origin feature/nome-da-feature  

---

## 🔀 Merge (simulando Pull Request)

Fluxo:

1. Finalizar feature  
2. Revisar código  
3. Fazer merge  

git checkout develop  
git merge feature/nome-da-feature  

---

## 🧹 Deletar branch

Após merge:

git branch -d feature/nome-da-feature  

---

## 🧠 Organização por Etapa

### Etapa 1 — Branches sugeridas

feature/project-setup  
feature/health-check  
feature/automation-schemas  
feature/automation-service  
feature/automation-routes  

---

## 🧠 Estratégia Profissional

Para subir seu nível:

- Separar commits por responsabilidade:
  - schemas
  - services
  - routes

- Evitar misturar tudo em um único commit

---

## 🚀 Resultado Esperado

Seguindo esse padrão você:

- Demonstra experiência real com Git
- Facilita leitura do projeto
- Simula ambiente de equipe
- Ganha vantagem em entrevistas

---

## 📍 Regra Final

Se alguém olhar seu GitHub, deve entender o projeto apenas pelos commits.