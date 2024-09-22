from httpx import AsyncClient
import asyncio
from faker import Faker

fake = Faker()


client = AsyncClient(base_url="http://127.0.0.1:8000/")


async def create_books():
    rsp = await client.post(
        url="/books/",
        json={
            "name": fake.sentence(nb_words=4),  # Fake book title with 4 words
            "author": fake.name(),  # Fake author name
            "isbn": fake.isbn13(),  # Fake ISBN number
            "genre": [fake.word(), fake.word()],  # Two fake genres
            "summary": fake.paragraph(),  # Fake book summary
            "page_count": fake.random_int(
                min=50, max=500
            ),  # Random page count between 50 and 500
        },
    )
    return rsp.json()


async def create_multiple_books(n):
    tasks = [create_books() for _ in range(n)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


asyncio.run(create_multiple_books(200))
