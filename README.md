# 💰 FinBot — Assistente Financeiro com IA

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red.svg)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/IA-Groq%20%7C%20Ollama-green.svg)](https://console.groq.com/)
[![DIO](https://img.shields.io/badge/Desafio-DIO-purple.svg)](https://www.dio.me/)

Assistente financeiro pessoal com IA generativa, desenvolvido como parte do desafio **BIA do Futuro** da plataforma **DIO**. Combina um **chat inteligente personalizado** com um **dashboard visual interativo** para acompanhamento financeiro em tempo real.

---

## ✨ Diferenciais do Projeto

- 🚀 **Groq API (gratuita)** — respostas em menos de 1 segundo, muito mais rápido que modelos locais
- 📊 **Dashboard visual** com gráficos interativos (gauge, pizza, barras)
- 🎯 **Contexto personalizado** — a IA conhece seu perfil, metas e produtos antes de responder
- ⚡ **Perguntas rápidas** — botões de atalho para as dúvidas mais comuns
- 🔄 **Dual provider** — funciona com Groq (nuvem) ou Ollama (local), você escolhe
- 🏦 **Catálogo de produtos** com indicação baseada no perfil do investidor

---

## 🚀 Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| 💬 **Chat com IA personalizado** | Conversa em linguagem natural com contexto completo do perfil financeiro |
| ⚡ **Perguntas rápidas** | Atalhos para as dúvidas mais comuns sobre metas e investimentos |
| 📊 **Dashboard interativo** | Gráficos de progresso da reserva, metas e análise de gastos |
| 🏦 **Catálogo de produtos** | Produtos financeiros com indicação baseada no perfil do investidor |
| ❓ **FAQ inteligente** | Perguntas frequentes sobre Tesouro Selic, CDB, FIIs e mais |
| 🔄 **Histórico de conversa** | Contexto mantido durante toda a sessão |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| 🐍 **Python 3.10+** | Linguagem principal |
| 🖥️ **Streamlit** | Interface web interativa |
| ⚡ **Groq API** | LLM em nuvem — ultra rápido e gratuito |
| 🤖 **Ollama** | Alternativa local (llama3.2, mistral, phi3) |
| 📈 **Plotly** | Gráficos interativos (gauge, pizza, barras) |
| 🐼 **Pandas** | Manipulação e análise dos dados financeiros |

---

## 📂 Estrutura do Projeto

```
finbot-assistente-financeiro/
│
├── app.py                        # Arquivo principal Streamlit
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação
│
├── data/                         # Dados do cliente (simulados)
│   ├── perfil_investidor.json    # Perfil, metas e patrimônio
│   ├── produtos_financeiros.json # Produtos disponíveis
│   ├── transacoes.csv            # Histórico de transações
│   └── historico_atendimento.csv # Histórico de atendimentos
│
└── modules/                      # Módulos da aplicação
    ├── ai_client.py              # Cliente IA (Groq + Ollama)
    ├── chat.py                   # Interface do chat
    ├── dashboard.py              # Dashboard com gráficos
    ├── produtos.py               # Catálogo de produtos e FAQ
    └── data_loader.py            # Carregamento dos dados
```

---

## ▶️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/marcuspaiv/finbot-assistente-financeiro.git
cd finbot-assistente-financeiro
```

### 2. Crie o ambiente virtual e instale as dependências

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 3. Configure a IA (escolha uma opção)

**Opção A — Groq (Recomendado ⚡ — gratuito e rápido):**
- Acesse [console.groq.com](https://console.groq.com) e crie uma conta gratuita
- Gere uma API Key
- Cole a chave na barra lateral do app ao executar

**Opção B — Ollama (local):**
- Certifique-se que o Ollama está instalado e rodando: `ollama serve`
- Tenha um modelo baixado: `ollama pull llama3.2`
- Selecione "Ollama (Local)" na barra lateral do app

### 4. Execute o app

```bash
streamlit run app.py
```

Acesse em: `http://localhost:8501`

---

## 📊 Exemplos de Perguntas ao FinBot

- 💬 *"Quanto falta para completar minha reserva de emergência?"*
- 💬 *"Qual produto você me recomenda agora dado meu perfil?"*
- 💬 *"Estou no caminho certo para comprar o apartamento?"*
- 💬 *"Me explique o Tesouro Selic de forma simples."*
- 💬 *"Quais foram meus maiores gastos este mês?"*

---

## 🔑 Por que Groq em vez de Ollama?

| Critério | Groq (nuvem) | Ollama (local) |
|----------|-------------|----------------|
| ⚡ Velocidade | < 1 segundo | 5–30 segundos |
| 💰 Custo | Gratuito (tier free) | Gratuito |
| 🔒 Privacidade | Dados na nuvem | 100% local |
| 💻 Hardware | Não exige GPU | Exige RAM/GPU |
| 🌐 Internet | Necessária | Não necessária |

---

## 📌 Observações

- O projeto utiliza **dados fictícios** fornecidos pelo desafio DIO
- A IA é instruída com o perfil completo do cliente antes de cada resposta
- O Groq oferece **14.400 requisições gratuitas por dia** no plano free
- Para uso offline completo, utilize a opção Ollama

---

## 🧩 Melhorias Futuras

- [ ] Autenticação de usuário com múltiplos perfis
- [ ] Integração com APIs de cotação em tempo real
- [ ] Exportação de relatório financeiro em PDF
- [ ] Notificações de metas atingidas
- [ ] Versão mobile com Streamlit Cloud

---

## 👨‍💻 Autor

**Marcus Venicius Paiva Caldas**

- **GitHub:** [@marcuspaiv](https://github.com/marcuspaiv)
- **LinkedIn:** [Marcus Paiva](https://www.linkedin.com/in/marcus-paiva-b10339186/)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">
  <br>
  Feito com ☕ e 🐍 Python por <a href="https://github.com/marcuspaiv">Marcus Paiva</a>
</div>
