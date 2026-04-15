class ChatApp {
    constructor() {
        this.conversationId = this.generateId();
        this.conversations = [];
        this.currentTheme = localStorage.getItem('theme') || 'light';
        this.API_URL = 'http://localhost:8000/api';
        
        this.initElements();
        this.attachEventListeners();
        this.loadConversations();
        this.applyTheme();
    }
    
    initElements() {
        this.messagesContainer = document.getElementById('messagesContainer');
        this.messageInput = document.getElementById('messageInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.newChatBtn = document.getElementById('newChatBtn');
        this.themeToggle = document.getElementById('themeToggle');
        this.uploadBtn = document.getElementById('uploadBtn');
        this.fileInput = document.getElementById('fileInput');
        this.conversationsList = document.getElementById('conversationsList');
    }
    
    attachEventListeners() {
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        this.newChatBtn.addEventListener('click', () => this.createNewConversation());
        this.themeToggle.addEventListener('click', () => this.toggleTheme());
        this.uploadBtn.addEventListener('click', () => this.fileInput.click());
        this.fileInput.addEventListener('change', (e) => this.handleFileUpload(e));
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        
        if (!message) return;
        
        // Add user message to UI
        this.addMessageToUI('user', message);
        this.messageInput.value = '';
        
        // Show loading indicator
        this.showLoadingIndicator();
        
        try {
            const response = await fetch(`${this.API_URL}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    conversation_id: this.conversationId,
                    message: message,
                    theme: this.currentTheme
                })
            });
            
            if (!response.ok) {
                throw new Error('Erro ao enviar mensagem');
            }
            
            const data = await response.json();
            this.removeLoadingIndicator();
            this.addMessageToUI('assistant', data.message);
            
        } catch (error) {
            this.removeLoadingIndicator();
            this.addMessageToUI('assistant', `Erro: ${error.message}`);
            console.error('Error:', error);
        }
    }
    
    addMessageToUI(role, content) {
        // Remove welcome message if it exists
        const welcomeMsg = this.messagesContainer.querySelector('.welcome-message');
        if (welcomeMsg) {
            welcomeMsg.remove();
        }
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;
        
        messageDiv.appendChild(contentDiv);
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = new Date().toLocaleTimeString('pt-BR', {
            hour: '2-digit',
            minute: '2-digit'
        });
        
        messageDiv.appendChild(timeDiv);
        
        this.messagesContainer.appendChild(messageDiv);
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }
    
    showLoadingIndicator() {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message assistant';
        messageDiv.id = 'loading-indicator';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content loading';
        
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('div');
            dot.className = 'loading-dot';
            contentDiv.appendChild(dot);
        }
        
        messageDiv.appendChild(contentDiv);
        this.messagesContainer.appendChild(messageDiv);
        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }
    
    removeLoadingIndicator() {
        const loader = document.getElementById('loading-indicator');
        if (loader) {
            loader.remove();
        }
    }
    
    async handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        const formData = new FormData();
        formData.append('conversation_id', this.conversationId);
        formData.append('file', file);
        
        try {
            const response = await fetch(`${this.API_URL}/upload-document`, {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) {
                throw new Error('Erro ao fazer upload do arquivo');
            }
            
            const data = await response.json();
            this.addMessageToUI('assistant', `✓ Arquivo "${data.filename}" foi processado com sucesso!`);
            
        } catch (error) {
            this.addMessageToUI('assistant', `Erro ao fazer upload: ${error.message}`);
            console.error('Error:', error);
        }
        
        // Reset file input
        this.fileInput.value = '';
    }
    
    createNewConversation() {
        this.conversationId = this.generateId();
        this.messagesContainer.innerHTML = `
            <div class="welcome-message">
                <h1>ChatGPT Clone</h1>
                <p>Nova conversa iniciada. Comece digitando sua pergunta!</p>
            </div>
        `;
        this.messageInput.focus();
        this.saveConversation();
    }
    
    toggleTheme() {
        this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        this.applyTheme();
        localStorage.setItem('theme', this.currentTheme);
    }
    
    applyTheme() {
        const body = document.body;
        
        if (this.currentTheme === 'dark') {
            body.classList.add('dark-mode');
            this.themeToggle.textContent = '☀️';
        } else {
            body.classList.remove('dark-mode');
            this.themeToggle.textContent = '🌙';
        }
    }
    
    saveConversation() {
        const conversation = {
            id: this.conversationId,
            title: `Conversa - ${new Date().toLocaleDateString('pt-BR')}`,
            timestamp: Date.now()
        };
        
        this.conversations.push(conversation);
        localStorage.setItem('conversations', JSON.stringify(this.conversations));
        this.renderConversations();
    }
    
    loadConversations() {
        const saved = localStorage.getItem('conversations');
        this.conversations = saved ? JSON.parse(saved) : [];
        this.renderConversations();
    }
    
    renderConversations() {
        this.conversationsList.innerHTML = '';
        
        this.conversations.forEach(conv => {
            const item = document.createElement('div');
            item.className = `conversation-item ${conv.id === this.conversationId ? 'active' : ''}`;
            
            const titleSpan = document.createElement('span');
            titleSpan.textContent = conv.title;
            titleSpan.style.flex = '1';
            titleSpan.addEventListener('click', () => this.switchConversation(conv.id));
            
            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-conv-btn';
            deleteBtn.textContent = '✕';
            deleteBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.deleteConversation(conv.id);
            });
            
            item.appendChild(titleSpan);
            item.appendChild(deleteBtn);
            this.conversationsList.appendChild(item);
        });
    }
    
    switchConversation(id) {
        this.conversationId = id;
        this.renderConversations();
        // Load conversation history from server
        this.loadConversationHistory(id);
    }
    
    async loadConversationHistory(id) {
        try {
            const response = await fetch(`${this.API_URL}/conversations/${id}`);
            
            if (!response.ok) {
                throw new Error('Erro ao carregar conversa');
            }
            
            const data = await response.json();
            this.messagesContainer.innerHTML = '';
            
            data.messages.forEach(msg => {
                this.addMessageToUI(msg.role, msg.content);
            });
            
            if (data.messages.length === 0) {
                this.messagesContainer.innerHTML = `
                    <div class="welcome-message">
                        <h1>ChatGPT Clone</h1>
                        <p>Comece uma nova conversa!</p>
                    </div>
                `;
            }
            
        } catch (error) {
            console.error('Error:', error);
        }
    }
    
    deleteConversation(id) {
        this.conversations = this.conversations.filter(conv => conv.id !== id);
        localStorage.setItem('conversations', JSON.stringify(this.conversations));
        
        if (id === this.conversationId) {
            this.createNewConversation();
        } else {
            this.renderConversations();
        }
        
        // Optional: delete from server
        fetch(`${this.API_URL}/conversations/${id}`, {
            method: 'DELETE'
        }).catch(console.error);
    }
    
    generateId() {
        return 'conv_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.chatApp = new ChatApp();
});
