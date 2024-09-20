import asyncio
import time
import httpx
from fastapi import FastAPI

app = FastAPI()

# Simulated external API endpoint
SIMULATED_API = "https://jsonplaceholder.typicode.com/comments"

@app.get("/blocking-fetch")
def blocking_fetch():
    response = httpx.get(SIMULATED_API)
    time.sleep(2)  # Simulate blocking delay
    return response.json()

@app.get("/non-blocking-fetch")
async def non_blocking_fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get(SIMULATED_API)
        await asyncio.sleep(2)  # Simulate non-blocking delay
        return response.json()
