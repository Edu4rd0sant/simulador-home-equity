import requests
import time
import hashlib
import json

# --- CONFIGURAÇÃO (Aqui você usaria variáveis de ambiente em produção) ---
ACCESS_TOKEN = 'SEU_TOKEN_DE_ACESSO_META'
PIXEL_ID = 'SEU_PIXEL_ID'
API_VERSION = 'v19.0'

# URL da API de Conversões do Facebook (CAPI)
url = f"https://graph.facebook.com/{API_VERSION}/{PIXEL_ID}/events"

def hash_data(data):
    """O Facebook exige que dados pessoais (email, tel) sejam criptografados em SHA256"""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def send_offline_conversion(user_data, event_name, value):
    """
    Envia um sinal para o Facebook quando um contrato é fechado no Banco.
    Isso ajuda o algoritmo a encontrar mais pessoas com perfil de 'Aprovado'.
    """
    
    payload = {
        "data": [
            {
                "event_name": event_name,
                "event_time": int(time.time()),
                "action_source": "physical_store", # Ou 'system_generated' para CRM
                "user_data": {
                    "em": [hash_data(user_data['email'])],
                    "ph": [hash_data(user_data['phone'])]
                },
                "custom_data": {
                    "currency": "BRL",
                    "value": value,
                    "contrato_tipo": "Home Equity"
                }
            }
        ],
        "access_token": ACCESS_TOKEN
    }

    try:
        response = requests.post(url, json=payload)
        print(f"Status: {response.status_code} - Resposta: {response.text}")
    except Exception as e:
        print(f"Erro ao conectar com Meta API: {e}")

# --- SIMULAÇÃO DE LEITURA DO BANCO DE DADOS ---
# Num cenário real, aqui teria um `cursor.execute("SELECT * FROM contratos WHERE status='assinado'")`

novos_contratos = [
    {"email": "cliente1@email.com", "phone": "5582999999999", "valor_ltv": 150000.00},
    {"email": "cliente2@email.com", "phone": "5582988888888", "valor_ltv": 80000.00}
]

print("--- Iniciando Sincronização de Contratos Fechados ---")

for contrato in novos_contratos:
    print(f"Enviando conversão de: {contrato['email']}")
    # Envia o evento 'Purchase' (Compra) com o valor do contrato
    send_offline_conversion(contrato, "Purchase", contrato['valor_ltv'])
    
print("--- Sincronização Finalizada ---")