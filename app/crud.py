from sqlalchemy.orm import Session
from . import models, schemas


def get_item(db: Session, item_id: int):
    """
    Retrieve a single item by its ID.
    
    Args:
        db: Database session
        item_id: ID of the item to retrieve
        
    Returns:
        Item object if found, None otherwise
    """
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of items with pagination.
    
    Args:
        db: Database session
        skip: Number of records to skip (offset)
        limit: Maximum number of records to return
        
    Returns:
        List of Item objects
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    """
    Create a new item in the database.
    
    Args:
        db: Database session
        item: Pydantic schema with item data
        
    Returns:
        The created Item object
    """
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    """
    Update an existing item in the database.
    
    Args:
        db: Database session
        item_id: ID of the item to update
        item: Pydantic schema with updated item data
        
    Returns:
        The updated Item object if found, None otherwise
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
        db.commit()
        db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    """
    Delete an item from the database.
    
    Args:
        db: Database session
        item_id: ID of the item to delete
        
    Returns:
        The deleted Item object if found, None otherwise
    """
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item