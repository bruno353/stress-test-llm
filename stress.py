import aiohttp
import asyncio
import time
import statistics
from datetime import datetime

N_REQUESTS = 10
PAYLOAD = {
    "model": "qwen2.5:32b",
    "messages": [
        {"role": "user", "content": "Tell me a quick joke"}
    ]
}

async def make_request(session, request_id):
    start_time = time.time()
    try:
        async with session.post(
            'http://localhost:11434/v1/chat/completions',
            json=PAYLOAD,
            headers={'Content-Type': 'application/json'}
        ) as response:
            await response.json()
            duration = time.time() - start_time
            print(f"Request {request_id} completed in {duration:.2f} seconds")
            return duration
    except Exception as e:
        print(f"Request {request_id} failed: {str(e)}")
        return None

async def main():
    print(f"\nStarting stress test with {N_REQUESTS} parallel requests at {datetime.now()}")
    print("=" * 50)
    
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, i) for i in range(N_REQUESTS)]
        durations = await asyncio.gather(*tasks)
        
        # Remove None values (failed requests)
        durations = [d for d in durations if d is not None]
        
        if durations:
            print("\nResults:")
            print(f"Average response time: {statistics.mean(durations):.2f} seconds")
            print(f"Min response time: {min(durations):.2f} seconds")
            print(f"Max response time: {max(durations):.2f} seconds")
            print(f"Standard deviation: {statistics.stdev(durations):.2f} seconds")
            print(f"Total successful requests: {len(durations)}")
            print(f"Failed requests: {N_REQUESTS - len(durations)}")
        else:
            print("\nAll requests failed!")

if __name__ == "__main__":
    asyncio.run(main())
