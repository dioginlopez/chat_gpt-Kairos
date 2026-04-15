# Guia de Desenvolvimento

## Configuração de ambiente para desenvolvimento

### 1. Clonar repositório
```bash
git clone <seu-repositorio>
cd chatgpt
```

### 2. Criar e ativar ambiente virtual

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Edite .env e adicione sua chave OpenAI
```

## Estrutura do projeto

### Backend (Python/FastAPI)
- `main.py` - Aplicação principal e endpoints
- `models.py` - Modelos de dados (Pydantic)
- `config.py` - Configurações centr alizadas
- `database.py` - Camada de persistência (SQLAlchemy)
- `document_handler.py` - Processamento de arquivos

### Frontend (HTML/CSS/JavaScript)
- `index.html` - Estrutura HTML
- `css/style.css` - Estilos (light/dark mode)
- `js/script.js` - Lógica da aplicação (classe ChatApp)

## Rodando localmente

### Terminal 1: Backend
```bash
cd backend
python main.py
```

### Terminal 2: Frontend (opcional - abra em navegador)
- Vá para `http://localhost:8000` ou abra `frontend/index.html`

## Convenções de código

### Python
- Usar snake_case para variáveis e funções
- Adicionar type hints
- Documentar funções com docstrings

### JavaScript
- Usar camelCase para variáveis e funções
- Usar comentários para código complexo
- Estruturado em clase `ChatApp`

## Testando endpoints

### Via curl
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"conversation_id":"test","message":"Olá","theme":"light"}'
```

### Via Python
```python
import requests

response = requests.post('http://localhost:8000/api/chat', json={
    'conversation_id': 'test',
    'message': 'Olá',
    'theme': 'light'
})
print(response.json())
```

## Adicionando novas funcionalidades

### 1. Novo endpoint HTTP
Edite `backend/main.py`:
```python
@app.post("/api/nova-funcao")
async def nova_funcao(dados: SeuModelo):
    try:
        # Sua lógica aqui
        return {"resultado": "sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 2. Novo modelo de dados
Edite `backend/models.py`:
```python
class NovoModelo(BaseModel):
    campo1: str
    campo2: int
    campo3: Optional[str] = None
```

### 3. Novo componente frontend
Edite `frontend/static/js/script.js` e adicione método à classe `ChatApp`

## Debugando

### Backend
```python
# Adicionar print para debug
print(f"DEBUG: variável = {variável}")

# Usar logging
import logging
logging.debug("Mensagem de debug")
```

### Frontend
- Abra DevTools (F12)
- Verifique Console para erros
- Use `console.log()` para debug

## Deploying

### Heroku
1. Criar conta em heroku.com
2. Instalar Heroku CLI
3. `heroku login`
4. `heroku create seu-app-name`
5. `git push heroku main`

### Railway/Render
Similares ao Heroku - seguir suas documentações específicas

## Próximas funcionalidades sugeridas

- [ ] Autenticação de usuários
- [ ] Compartilhamento de conversas
- [ ] Integração com mais APIs (Google Gemini, Claude)
- [ ] Análise de sentimento
- [ ] Sistema de plugins
- [ ] Export de conversas (PDF, JSON)
