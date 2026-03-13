# 🤖 Lisboadas Auto-Staff Bot

Automação reativa para o sistema de Whitelist da **Lisboadas Cloud**. Desenvolvido em Python para otimizar o fluxo de trabalho de staffs em servidores de FiveM.

## ✨ Funcionalidades
- **Gatilho Reativo**: Detecta o alerta do site e age apenas quando necessário (evita F5 constante).
- **Segurança**: Delay configurável para respeitar os limites do servidor.
- **Discord Integration**: Logs em tempo real via Webhook.

## 🛠️ Instalação
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Instale os navegadores: `playwright install`.

## ⚙️ Como Usar
1. Gere seu arquivo de sessão:
   `python -m playwright codegen https://whitelist.lisboadas.cloud/server --save-storage=auth.json`
2. Logue no painel e feche o navegador.
3. Inicie o bot: `python bot_whitelist.py`.
