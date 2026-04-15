# 🚀 Comece Aqui!

Seu ChatGPT Clone foi criado com sucesso! O servidor está rodando em **http://localhost:8000**

## ⚡ Próximos passos (2 minutos):

### 1️⃣ Adicionar sua chave de API
Edite o arquivo `.env`:
```
OPENAI_API_KEY=sk-sua-chave-aqui
```

**Obter chave:**
- Vá para https://platform.openai.com/api-keys
- Crie uma nova chave
- Cole em `.env`

### 2️⃣ Abrir a interface
- **Web**: http://localhost:8000
- **Ou abra**: `frontend/index.html` localmente

### 3️⃣ Testar!
- Digite uma mensagem e envie
- Teste upload de arquivo (PDF, TXT, DOCX)
- Mude de tema (🌙)

## 📁 Arquivos importantes:

| Arquivo | O quê |
|---------|-------|
| `.env` | Sua chave OpenAI vai aqui ⭐️ |
| `backend/main.py` | Servidor FastAPI |
| `frontend/index.html` | Interface do chat |
| `README.md` | Documentação completa |
| `SETUP.md` | Guia de instalação |

## 🎨 Funcionalidades incluídas:

✅ Chat em tempo real com OpenAI  
✅ Histórico de conversas (JSON)  
✅ Múltiplos temas (light/dark)  
✅ Upload de documentos (PDF, DOCX, TXT)  
✅ Sistema de contexto inteligente  
✅ Interface responsiva (mobile-friendly)  

## 🔗 Links úteis:

- [Documentação FastAPI](https://fastapi.tiangolo.com)
- [API da OpenAI](https://platform.openai.com/docs)
- [Meu Projeto no GitHub](https://github.com)

## ❓ Problemas?

1. **"OPENAI_API_KEY not found"** → Edite `.env`
2. **"Connection refused"** → Servidor não está rodando
3. **Upload de PDF falha** → Instale: `pip install PyPDF2`
4. **Upload de DOCX falha** → Instale: `pip install python-docx`

## 💡 Dicas:

- O histórico fica em `chatgpt.json`
- Pressione ENTER para enviar mensagens
- Renovar chave OpenAI: https://platform.openai.com/api-keys

---

**Parabéns!** 🎉 Agora é só adicionar sua chave OpenAI e começar a usar!

Não esqueça de ler o [README.md](README.md) para mais detalhes.
