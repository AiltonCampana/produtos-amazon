import json
import os
import requests

# Configurações do Telegram
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# Exemplo de lista de produtos/ofertas (pode vir de API ou scraper)
OFERTAS = [
    {
        "id": "1",
        "titulo": "Echo Pop | Smart speaker compacto com Alexa",
        "preco": "R$ 215,10",
        "link": "https://www.amazon.com.br/dp/B09WX6B151?tag=SEU_TAG_AFILIADO",
        "imagem": "https://m.media-amazon.com/images/I/61N4j4vHbgL._AC_SL1000_.jpg",
    }
]


def enviar_telegram(produto):
    mensagem = f"🔥 *{produto['titulo']}*\n💰 Por apenas: *{produto['preco']}*\n\n🔗 [Garantir Oferta]({produto['link']})"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "photo": produto["imagem"],
        "caption": mensagem,
        "parse_mode": "Markdown",
    }
    requests.post(url, json=payload)


def atualizar_landing_page(produtos):
    # Salva os dados em um JSON para o index.html carregar via JS
    with open("produtos.json", "w", encoding="utf-8") as f:
        json.dump(produtos, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    for produto in OFERTAS:
        enviar_telegram(produto)
    atualizar_landing_page(OFERTAS)
