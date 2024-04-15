import time

from fastapi import Request

from utils import format_process_time


async def time_to_complete(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)

    processing_time = time.time() - start_time
    format_processing_time = await format_process_time(duration=processing_time)
    print(f"\nprocess time: {format_processing_time}\n")

    return response
