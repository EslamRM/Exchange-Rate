import requests


class ExchangeRateService:
    BASE_URL = "https://api.exchangerate-api.com/v4/latest/USD"
    API_KEY = "YOUR_API_KEY"

    @classmethod
    def get_exchange_rate(cls, base_currency: str, target_currency: str):
        url = f"{cls.BASE_URL}/latest.json"
        params = {"app_id": cls.API_KEY, "base": base_currency.upper()}
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise ValueError("Failed to fetch exchange rates")
        data = response.data
        rate = data["rates"].get(target_currency.upper())

        if rate is None:
            raise ValueError(f"Currency {target_currency} not found")

        return {
            "base": base_currency.upper(),
            "target": target_currency.upper(),
            "rate": rate,
            "timestamp": data.get("timestamp"),
        }
