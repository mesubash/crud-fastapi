# FastAPI CRUD Application

A simple CRUD (Create, Read, Update, Delete) API built with FastAPI, SQLAlchemy, and SQLite.

## Features

- ✅ Create, Read, Update, and Delete items
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Pydantic schemas for data validation
- ✅ Clean, modular project structure
- ✅ Automatic API documentation (Swagger UI)

## Project Structure

```
/my_fastapi_crud
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point for the FastAPI app
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations logic
│   ├── database.py      # Database configuration
│   └── api/
│       └── item.py      # Item routes
│
├── requirements.txt
└── README.md
```

## Installation

1. **Clone or create the project directory**

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the development server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Items

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint (health check) |
| POST | `/items/` | Create a new item |
| GET | `/items/` | Get all items (with pagination) |
| GET | `/items/{item_id}` | Get a specific item by ID |
| PUT | `/items/{item_id}` | Update an item |
| DELETE | `/items/{item_id}` | Delete an item |

## Usage Examples

### Create an Item
```bash
curl -X POST "http://127.0.0.1:8000/items/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Sample Item", "description": "This is a sample item"}'
```

### Get All Items
```bash
curl "http://127.0.0.1:8000/items/"
```

### Get a Specific Item
```bash
curl "http://127.0.0.1:8000/items/1"
```

### Update an Item
```bash
curl -X PUT "http://127.0.0.1:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item", "description": "This item has been updated"}'
```

### Delete an Item
```bash
curl -X DELETE "http://127.0.0.1:8000/items/1"
```

## Database

The application uses SQLite as the database, which is stored in a file named `test.db` in the project root directory. The database and tables are created automatically when you first run the application.

## Development

To modify the application:

- **Add new models**: Edit `app/models.py`
- **Add new schemas**: Edit `app/schemas.py`
- **Add CRUD operations**: Edit `app/crud.py`
- **Add new routes**: Create new files in `app/api/` and include them in `app/main.py`

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type hints

## License

This project is open source and available for educational purposes.