# Setup Guide - ChatGPT Clone

## Pré-requisitos Instalados ✓
- Python 3.14.4
- Virtual Environment configurado
- Todas as dependências instaladas

## Próximos passos:

### 1. Obter chave de API da OpenAI
1. Acesse https://platform.openai.com/api-keys
2. Faça login ou crie uma conta
3. Clique em "Create new secret key"
4. Copie a chave gerada

### 2. Configurar variável de ambiente
Edite o arquivo `.env` neste diretório e adicione sua chave:
```
OPENAI_API_KEY=sk-sua-chave-aqui
```

### 3. Iniciar o servidor
Execute no terminal (a partir do diretório raiz):
```bash
cd backend
c:/Users/diogi/OneDrive/Documentos/chatgpt/.venv/Scripts/python.exe main.py
```

Você deve ver:
```
✓ ChatGPT Clone iniciado com sucesso
Uvicorn running on http://127.0.0.1:8000
```

### 4. Acessar a aplicação
Abra seu navegador e vá para:
- **Interface web**: http://localhost:8000 (ou abra `frontend/index.html`)
- **API docs**: http://localhost:8000/docs
- **Health check**: http://localhost:8000/api/health

### 5. Testar a aplicação
- Digite uma mensagem no chat
- Verifique a resposta da IA
- Teste upload de documento (PDF, TXT, DOCX)
- Teste a alternância de tema (🌙 em cima à esquerda)

## Estrutura dos arquivos:

```
chatgpt/
├── backend/
│   ├── main.py              # Servidor FastAPI
│   ├── models.py            # Modelos de dados
│   ├── config.py            # Configuração
│   ├── database.py          # Banco de dados
│   └── document_handler.py  # Processamento de docs
├── frontend/
│   └── static/
│       ├── index.html       # Interface
│       ├── css/style.css    # Estilos
│       └── js/script.js     # Lógica
├── docs/
│   ├── README.md            # Documentação completa
│   ├── DEVELOPMENT.md       # Guia de desenvolvimento
│   └── CHECKLIST.md         # Checklist de testes
├── .env                     # Variáveis de ambiente (EDITAR AQUI!)
├── requirements.txt         # Dependências
└── README.md               # Leia primeiro!
```

## Solução de problemas:

**"OPENAI_API_KEY not found"**
- Verifique se preencheu o arquivo `.env` corretamente
- Confirme que não há espaços extras na chave

**"Connection refused"**
- Certifique-se que o servidor está rodando em outro terminal
- Verifique se a porta 8000 está disponível

**"ModuleNotFoundError"**
- Ative o ambiente virtual: `.\venv\Scripts\Activate.ps1`
- Reinstale dependências: `pip install -r requirements.txt`

## Comandos úteis:

```bash
# Ativar ambiente virtual (Windows)
.\venv\Scripts\Activate.ps1

# Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate

# Desativar ambiente virtual
deactivate

# Iniciar servidor
cd backend && python main.py

# Ver documentação de APIs
# Vá para: http://localhost:8000/docs
```

## Próximas funcionalidades para adicionar:

- [ ] Autenticação de usuários
- [ ] Múltiplos modelos de IA (GPT-4, Claude, etc)
- [ ] Compartilhamento de conversas
- [ ] Export de conversas (PDF)
- [ ] Sistema de plugins
- [ ] Busca por conversas antigas

## Documentação útil:

- FastAPI: https://fastapi.tiangolo.com
- OpenAI API: https://platform.openai.com/docs/api-reference
- Pydantic: https://docs.pydantic.dev
- SQLAlchemy: https://www.sqlalchemy.org

---
**Parabéns!** Seu chatbot está pronto. Comece agora adicionando sua chave OpenAI no arquivo `.env`! 🚀
