# ChatGPT Clone

Um chatbot inteligente construído com Python, FastAPI e OpenAI API, com interface web moderna, histórico de conversas, suporte a múltiplos temas e integração com documentos.

## 🚀 Funcionalidades

- ✨ **Chat em tempo real** com OpenAI GPT-3.5-turbo
- 💾 **Histórico de conversas** persistente com banco de dados SQLite
- 🎨 **Temas personalizáveis** (light/dark mode)
- 📄 **Integração com documentos** (PDF, DOCX, TXT, Markdown)
- 🧠 **Sistema de contexto** que mantém histórico recente nas conversas
- 📱 **Interface responsiva** que funciona em desktop e mobile
- 🔒 **CORS habilitado** para segurança

## 📋 Requisitos

- Python 3.8+
- pip ou conda
- Chave de API da OpenAI

## 🔧 Instalação

### 1. Clonar e organizar o projeto

```bash
cd chatgpt
```

### 2. Criar ambiente virtual

**Windows (PowerShell):**
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

Copie `.env.example` para `.env` e adicione sua chave de API:

```bash
cp .env.example .env
```

Edite `.env` e adicione sua chave OpenAI:
```
OPENAI_API_KEY=sk-seu-chave-api-aqui
```

**Como obter a chave:**
1. Vá para https://platform.openai.com/api-keys
2. Crie uma nova chave de API
3. Copie e cole em seu arquivo `.env`

## 🚀 Executar

### Iniciar o servidor FastAPI

```bash
cd backend
python main.py
```

O servidor estará disponível em `http://localhost:8000`

### Acessar a interface web

1. Abra seu navegador
2. Vá para `http://localhost:8000/static/` ou abra `frontend/index.html`

## 📁 Estrutura do Projeto

```
chatgpt/
├── backend/
│   ├── main.py                 # Aplicação FastAPI principal
│   ├── models.py              # Modelos Pydantic
│   ├── config.py              # Configurações da aplicação
│   ├── database.py            # Operações de banco de dados
│   └── document_handler.py    # Processamento de documentos
├── frontend/
│   └── static/
│       ├── index.html         # Interface web
│       ├── css/
│       │   └── style.css      # Estilos
│       └── js/
│           └── script.js      # Lógica do frontend
├── docs/                      # Documentação
├── requirements.txt           # Dependências Python
├── .env.example              # Exemplo de variáveis de ambiente
└── README.md                 # Este arquivo
```

## 🔌 Endpoints da API

### Chat
- **POST** `/api/chat` - Enviar mensagem
  ```json
  {
    "conversation_id": "conv_123",
    "message": "Olá, como você está?",
    "theme": "light"
  }
  ```

### Conversas
- **GET** `/api/conversations/{conversation_id}` - Obter histórico
- **DELETE** `/api/conversations/{conversation_id}` - Deletar conversa

### Documentos
- **POST** `/api/upload-document` - Upload de arquivo
  - Formatos suportados: PDF, DOCX, TXT, Markdown

### Health Check
- **GET** `/api/health` - Verificar status do servidor

## 🎨 Personalização

### Mudar tema padrão
Edite `frontend/static/js/script.js` e mude:
```javascript
this.currentTheme = localStorage.getItem('theme') || 'dark'; // Mude para 'dark'
```

### Aumentar limite de contexto
Edite `.env`:
```
CONTEXT_MEMORY_SIZE=20  # Aumenta de 10 para 20 mensagens
```

### Usar outro modelo
Edite `backend/main.py` e mude:
```python
model="gpt-4"  # ou "gpt-3.5-turbo"
```

## 🐛 Troubleshooting

### Erro: "OPENAI_API_KEY not found"
- Verifique se criou o arquivo `.env` corretamente
- Confirme que adicionou sua chave de API válida

### Erro: "Connection refused"
- Certifique-se que o servidor está rodando (`localhost:8000`)
- Verifique se a porta 8000 não está em uso

### Erro ao fazer upload de PDF
- Instale PyPDF2: `pip install PyPDF2`

### Erro ao fazer upload de DOCX
- Instale python-docx: `pip install python-docx`

## 📊 Desenvolvimento

### Dependências principais
- **FastAPI** - Framework web
- **Uvicorn** - Servidor ASGI
- **OpenAI** - API de IA
- **SQLAlchemy** - ORM para banco de dados
- **Pydantic** - Validação de dados

## 📝 Licença

Este projeto é fornecido como exemplo educacional.

## 🤝 Contribuições

Sinta-se livre para fazer fork, melhorar e enviar pull requests!

## 📞 Suporte

Para problemas ou dúvidas:
1. Verifique a seção de Troubleshooting
2. Consulte a documentação da OpenAI: https://platform.openai.com/docs
3. Verifique a documentação do FastAPI: https://fastapi.tiangolo.com
