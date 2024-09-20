import asyncio
import time
from contextlib import contextmanager
from multiprocessing import Process
import uvicorn
from httpx import AsyncClient
from src.app import app

def start_server():
    uvicorn.run(app, port=8000, log_level="error")

@contextmanager
def run_server_context():
    process = Process(target=start_server)
    process.start()
    time.sleep(3)  # Allow the server to start properly
    print("FastAPI server is running in a separate process")
    yield
    process.terminate()

async def send_requests(endpoint_count: int, endpoint_path: str):
    async with AsyncClient(base_url="http://localhost:8000") as client:
        tasks = (client.get(endpoint_path, timeout=float("inf")) for _ in range(endpoint_count))
        await asyncio.gather(*tasks)

async def benchmark(endpoint_count: int = 100):
    with run_server_context():
        start_time = time.time()
        await send_requests(endpoint_count, "/blocking-fetch")
        end_time = time.time()
        print(f"Time taken to make {endpoint_count} requests to blocking-fetch endpoint: {end_time - start_time} seconds")

        start_time = time.time()
        await send_requests(endpoint_count, "/non-blocking-fetch")
        end_time = time.time()
        print(f"Time taken to make {endpoint_count} requests to non-blocking-fetch endpoint: {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(benchmark(endpoint_count=1000))
