from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int | None = None
    name: str
    description: str | None


items = [
    *[
        Item(id=i, name="Plumbus", description="A multi-purpose household device.")
        for i in range(10**6)
    ],
    *[
        Item(id=i, name="Portal Gun", description="A portal opening device.")
        for i in range(10**6)
    ],
    *[
        Item(id=i, name="Meeseeks Box", description="A box that summons a Meeseeks.")
        for i in range(10**6)
    ]
]


@app.get("/items/stream")
async def stream_items() -> AsyncIterable[Item]:
    for item in items:
        yield item
