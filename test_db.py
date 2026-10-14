import asyncio
from sqlalchemy import text
from src.db.main import engine

async def main():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print(result.scalar())

asyncio.run(main())