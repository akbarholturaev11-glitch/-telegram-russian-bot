from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable


class DBSessionMiddleware(BaseMiddleware):
    def __init__(self, sessionmaker):
        self.sessionmaker = sessionmaker

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any]
    ):
        async with self.sessionmaker() as session:
            data["session"] = session
            return await handler(event, data)
