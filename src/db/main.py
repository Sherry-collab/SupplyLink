from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import Config

# 1. Sadak: ek hi baar banti hai
engine = create_async_engine(Config.DATABASE_URL, echo=True)

# 2. Phone banane ki machine: ek hi baar banti hai
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# 3. Receptionist: har request ko ek phone deta hai
async def get_session():
    async with SessionLocal() as session:
        yield session


