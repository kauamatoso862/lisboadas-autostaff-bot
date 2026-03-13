import asyncio
import requests
import os
from playwright.async_api import async_playwright

# --- CONFIGURAÇÕES ---
DISCORD_WEBHOOK_URL = "SUA_URL_DO_WEBHOOK_AQUI" 
URL_PAINEL = "https://whitelist.lisboadas.cloud/server"
DELAY_SEGURANCA = 20 
# ---------------------

def enviar_discord(msg):
    if DISCORD_WEBHOOK_URL and "discord.com" in DISCORD_WEBHOOK_URL:
        payload = {
            "embeds": [{
                "title": "🤖 Lisboadas Auto-Staff",
                "description": msg,
                "color": 3066993,
                "footer": {"text": "Automação via Playwright"}
            }]
        }
        try: requests.post(DISCORD_WEBHOOK_URL, json=payload)
        except: print("❌ Falha ao enviar Webhook.")

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(storage_state="auth.json")
        page = await context.new_page()

        print("🚀 Bot iniciado! Aguardando notificação...")
        await page.goto(URL_PAINEL)

        while True:
            try:
                # 1. Espera o gatilho visual do 'apito' (atualizar dados)
                gatilho = page.get_by_text("atualizar os dados agora")
                await gatilho.wait_for(state="visible", timeout=0)
                
                print("🔔 Notificação detectada! Carregando player...")
                await gatilho.click()

                # 2. Localiza e clica no player
                player_link = page.locator(".compact-list.read a").first
                await player_link.wait_for(state="visible", timeout=15000)
                
                info = await player_link.inner_text()
                await player_link.click()

                # 3. Paciência para o modal abrir
                await page.wait_for_timeout(2000)

                # 4. Aprovação
                btn_aprovar = page.get_by_role("button", name=" Aprovar")
                await btn_aprovar.wait_for(state="visible", timeout=5000)
                await btn_aprovar.click()
                
                print(f"✅ Aprovado: {info}")
                enviar_discord(f"Whitelist aprovada: **{info}**")

                # 5. Reset e Delay
                await page.wait_for_timeout(2000)
                await page.goto(URL_PAINEL)
                await asyncio.sleep(DELAY_SEGURANCA)

            except Exception as e:
                print(f"🔄 Reiniciando modo de espera...")
                await page.goto(URL_PAINEL)
                await asyncio.sleep(10)

asyncio.run(run())
