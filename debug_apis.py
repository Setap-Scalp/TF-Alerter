import requests
import json
from datetime import datetime

print("=" * 80)
print("BINANCE FUNDING RATES")
print("=" * 80)
try:
    response = requests.get(
        "https://fapi.binance.com/fapi/v1/fundingRate?limit=3", timeout=5
    )
    print(f"Status: {response.status_code}")
    data = response.json()
    print(json.dumps(data[:2] if isinstance(data, list) else data, indent=2))
except Exception as e:
    print(f"ERROR: {e}")

print("\n" + "=" * 80)
print("BYBIT MARKET TICKERS")
print("=" * 80)
try:
    response = requests.get(
        "https://api.bybit.com/v5/market/tickers?category=linear", timeout=5
    )
    print(f"Status: {response.status_code}")
    data = response.json()
    if "result" in data:
        items = data["result"].get("list", [])[:2]
        print(json.dumps({"result": {"list": items}}, indent=2))
    else:
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"ERROR: {e}")

print("\n" + "=" * 80)
print("OKX FUNDING RATE")
print("=" * 80)
try:
    response = requests.get("https://www.okx.com/api/v5/public/funding-rate", timeout=5)
    print(f"Status: {response.status_code}")
    data = response.json()
    if "data" in data:
        print(json.dumps({"data": data["data"][:2]}, indent=2))
    else:
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"ERROR: {e}")

print("\n" + "=" * 80)
print("GATE.IO FUNDING RATES")
print("=" * 80)
try:
    response = requests.get(
        "https://api.gateio.ws/api/v4/futures/usdt/funding_rates", timeout=5
    )
    print(f"Status: {response.status_code}")
    data = response.json()
    print(json.dumps(data[:2] if isinstance(data, list) else data, indent=2))
except Exception as e:
    print(f"ERROR: {e}")

print("\n" + "=" * 80)
print("BITGET CURRENT FUND RATE")
print("=" * 80)
try:
    response = requests.get(
        "https://api.bitget.com/api/v2/mix/market/current-fund-rate?productType=umcbl",
        timeout=5,
    )
    print(f"Status: {response.status_code}")
    data = response.json()
    if "data" in data:
        print(json.dumps({"data": data["data"][:2]}, indent=2))
    else:
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"ERROR: {e}")

print("\n" + "=" * 80)
print("Current time:", datetime.now())
print("=" * 80)
