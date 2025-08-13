from sqlalchemy import String, Text, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from .db import Base

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True)
    quotes = relationship("Quote", back_populates="author")

class Quote(Base):
    __tablename__ = "quotes"
    __table_args__ = (UniqueConstraint("text"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    tags: Mapped[list[str]] = mapped_column(ARRAY(String(50)))
    source_url: Mapped[str] = mapped_column(String(500))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author = relationship("Author", back_populates="quotes")
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    