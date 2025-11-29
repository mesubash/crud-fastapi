from fastapi import FastAPI
from .database import engine, Base
from .api import item

# Create all database tables
# This will create the tables defined in models.py if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="FastAPI CRUD Application",
    description="A simple CRUD API with FastAPI and SQLAlchemy",
    version="1.0.0"
)

# Include the item router
app.include_router(item.router)


@app.get("/")
def root():
    """
    Root endpoint - health check.
    
    Returns:
        Welcome message
    """
    return {"message": "Welcome to FastAPI CRUD API"}