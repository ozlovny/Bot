import aiohttp
from config import CRYPTOBOT_API

async def verify_payment_fixed(user_id: int, bet: str) -> dict | None:
    url = "https://testnet-pay.crypt.bot/api/getPayments"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={"Crypto-Pay-API-Token": CRYPTOBOT_API}) as resp:
            if resp.status != 200:
                return None

            data = await resp.json()
            payments = data.get("result", [])

            for p in payments:
                if (
                    p.get("status") == "completed"
                    and p.get("comment", "").lower() == bet.lower()
                    and p.get("user_id") == user_id
                ):
                    return {
                        "amount": float(p.get("amount", 0)),
                        "currency": p.get("asset", "USDT"),
                        "payment_id": p.get("payment_id")
                    }

    return None