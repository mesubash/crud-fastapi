from sqlalchemy import Column, Integer, String
from .database import Base


class Item(Base):
    """
    SQLAlchemy model for the Item table.
    
    Attributes:
        id: Primary key, auto-incremented integer
        name: Name of the item (required)
        description: Description of the item (optional)
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)