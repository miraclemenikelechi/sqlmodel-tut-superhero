async def format_process_time(duration: int | float) -> str:
    minutes, seconds = divmod(duration, 60)
    milliseconds = (duration - int(duration)) * 1000
    return f"{int(minutes)}m:{int(seconds)}s:{int(milliseconds)}ms"
