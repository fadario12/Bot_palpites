import requests
from datetime import datetime

# 🔑 CONFIGURAÇÕES
API_FOOTBALL_KEY = "91897278d3071c6f55547f5f0450a8f6"
TELEGRAM_TOKEN = "7002883935:AAENPqwDs1-_LQlYq77jvxuNwnWgmWF4WQ4"
CHAT_ID = "-1002649180401"

# 📅 PEGAR A DATA DE HOJE
hoje = datetime.today().strftime('%Y-%m-%d')

# 📊 Buscar Partidas do Dia
def obter_jogos():
    url = f"https://v3.football.api-sports.io/fixtures?date={hoje}"
    headers = {"x-apisports-key": API_FOOTBALL_KEY}
    resposta = requests.get(url, headers=headers)
    dados = resposta.json()

    print("🔍 Dados recebidos da API:", dados)  # Debug

    jogos = []
    for match in dados.get("response", []):
        casa = match["teams"]["home"]["name"]
        visitante = match["teams"]["away"]["name"]
        jogos.append(f"{casa} vs {visitante}")

    return jogos

# 🔮 Gerar Palpites Simples
def gerar_palpite(jogos):
    palpites = []
    for jogo in jogos:
        casa, visitante = jogo.split(" vs ")
        palpite = f"Palpite: {casa} vence ou empate"
        palpites.append(palpite)
    return palpites

# 📩 Enviar para o Telegram usando requests
def enviar_para_telegram(palpites):
    for palpite in palpites:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": palpite}
        resposta = requests.post(url, data=data)
        print(f"📨 Enviado: {palpite} - Resposta: {resposta.json()}")  # Debug

# 📌 Executar Agora
def executar_bot():
    print(f"📅 Buscando jogos para {hoje}...")
    jogos = obter_jogos()
    if jogos:
        palpites = gerar_palpite(jogos)
        enviar_para_telegram(palpites)
        print("✅ Palpites enviados!")
    else:
        print("⚠️ Nenhum jogo encontrado para hoje.")

# 🚀 Rodar o código agora
executar_bot()
