import requests
import json

url = 

# Menü al
menu_request = {
    "jsonrpc": "2.0",
    "method": "getMenu",
    "id": 1
}
menu_response = requests.post(url, json=menu_request).json()
print("📋 Menü:", menu_response["result"])

# Sipariş gönder
order_request = {
    "jsonrpc": "2.0",
    "method": "order",
    "params": {"items": ["pizza", "kola"]},
    "id": 2
}
order_response = requests.post(url, json=order_request).json()
print("🧾 Yanıt:", order_response["result"])
