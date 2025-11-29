from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas
from ..database import get_db

# Create an APIRouter instance for item-related routes
router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.post("/", response_model=schemas.Item, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.
    
    Args:
        item: Item data from request body
        db: Database session (injected)
        
    Returns:
        The created item with its ID
    """
    return crud.create_item(db=db, item=item)


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of items with pagination.
    
    Args:
        skip: Number of records to skip (default: 0)
        limit: Maximum number of records to return (default: 100)
        db: Database session (injected)
        
    Returns:
        List of items
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single item by ID.
    
    Args:
        item_id: ID of the item to retrieve
        db: Database session (injected)
        
    Returns:
        The requested item
        
    Raises:
        HTTPException: 404 if item not found
    """
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Update an existing item.
    
    Args:
        item_id: ID of the item to update
        item: Updated item data from request body
        db: Database session (injected)
        
    Returns:
        The updated item
        
    Raises:
        HTTPException: 404 if item not found
    """
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item.
    
    Args:
        item_id: ID of the item to delete
        db: Database session (injected)
        
    Returns:
        The deleted item
        
    Raises:
        HTTPException: 404 if item not found
    """
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item