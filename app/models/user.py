from datetime import datetime

from sqlalchemy import BigInteger, func, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    __tablename__ = "user"

    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="alive")
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
    status_updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
