import fastapi
import httpx


async def checkSymbol(symbol: str):
    nasdaq_url = f"https://api.nasdaq.com/api/quote/{symbol}/info?assetclass=stocks"
    
    

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(nasdaq_url)
            resp.raise_for_status()
            nasdaq_client = resp.json() 
            return nasdaq_client
        except httpx.RequestError as exc:
            response = {
                "error": {
                    "code": 404,
                    "message": str(exc)
                }
            }
        return response

async def get_history(symbol:str):
    free_url ='https://finnhub.io/api/v1/stock/candle?symbol='+symbol+'&resolution=D&from=1580638400&to=1588180800&token=bq4h0lqrh5r8cj7k2b2r'
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(free_url)
            resp.raise_for_status()
            nasdaq_client = resp.json() 
            return nasdaq_client
        except httpx.RequestError as exc:
            response = {
                "error": {
                    "code": 404,
                    "message": str(exc)
                }
            }
        return response