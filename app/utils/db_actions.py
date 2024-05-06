from sqlalchemy import insert, select, func

from app.models import User
from app.schemas.user_schema import UserSchemaOutput
from app.settings import sessionmaker


async def get_or_create_user(telegram_id: int):
    async with sessionmaker() as session:
        user_query = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(user_query)
        user = result.scalar_one_or_none()

        if not user:
            query = (
                insert(User)
                .values(telegram_id=telegram_id)
                .returning(
                    User.id,
                    User.telegram_id,
                    User.created_at,
                    User.status_updated_at,
                    User.status,
                )
            )
            result = await session.execute(query)

            await session.commit()

            user = result.mappings().first()
            return UserSchemaOutput(**user)

        return UserSchemaOutput(**user.__dict__)


async def finish_user(telegram_id: int):
    async with sessionmaker() as session:
        user_query = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(user_query)
        user = result.scalar_one_or_none()

        if user:
            user.status = "finished"
            user.status_updated_at = func.now()

            await session.commit()
