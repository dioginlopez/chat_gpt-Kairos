# ChatGPT Clone - Deployment Guide

## Deploy no Render

### 1. Conectar GitHub
1. Vá para https://render.com
2. Clique em "New +"
3. Selecione "Web Service"
4. Conecte seu repositório GitHub: `chat_gpt-Kairos`

### 2. Configurar Build & Deploy
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port 10000`

### 3. Adicionar Variáveis de Ambiente
No painel do Render, adicione:
- **OPENAI_API_KEY**: Sua chave da OpenAI (como Secret)
- **DEBUG**: False (para produção)

### 4. Deploy
O Render fará deploy automático a cada push no GitHub! 🚀

### URLs após Deploy
- **App**: https://seu-app.onrender.com
- **API**: https://seu-app.onrender.com/api/health
- **Chat**: https://seu-app.onrender.com

## Deploy Local (teste antes)
```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Troubleshooting

### Erro: "No module named 'openai'"
- Certifique-se que `requirements.txt` está na raiz do projeto
- Execute: `pip install -r requirements.txt`

### Erro: "OPENAI_API_KEY not found"
- Adicione a variável de ambiente no painel do Render
- Não coloque no .env (que não é enviado para produção)

### App muito lento
- Use um plano pago no Render
- Otimize as requisições à OpenAI
