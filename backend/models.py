from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100))
    hospital = Column(String(150))
    location = Column(String(150))

    interactions = relationship(
        "Interaction",
        back_populates="hcp",
        cascade="all, delete-orphan"
    )


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_id = Column(
        Integer,
        ForeignKey("hcps.id"),
        nullable=False
    )

    interaction_type = Column(String(50), nullable=False)
    interaction_date = Column(Date, nullable=False)
    topics_discussed = Column(Text)
    sentiment = Column(String(50))
    summary = Column(Text)
    follow_up_date = Column(Date, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    hcp = relationship(
        "HCP",
        back_populates="interactions"
    )