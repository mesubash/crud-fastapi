from pydantic import BaseModel, ConfigDict
from typing import Optional


class ItemBase(BaseModel):
    """
    Base schema with common fields for Item.
    Used as a parent class for other Item schemas.
    """
    name: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """
    Schema for creating a new item.
    Inherits name and description from ItemBase.
    Used for request validation when creating items.
    """
    pass


class Item(ItemBase):
    """
    Schema for representing an item in responses.
    Includes the id field from the database.
    """
    id: int

    # Pydantic v2 configuration
    model_config = ConfigDict(from_attributes=True)