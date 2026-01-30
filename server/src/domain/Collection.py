from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_as_dataclass, mapped_column
from domain.db_registry import table_registry


@mapped_as_dataclass(table_registry)
class Collection:
    __tablename__ = "collections"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
