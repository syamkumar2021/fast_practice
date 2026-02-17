from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publish_date": "1988-01-01"
    },
    {
        "id": 2,
        "title": "The Dentist",
        "author": "Neal",
        "publish_date": "1995-06-20"
    },
    {
        "id": 3,
        "title": "The Chemist",
        "author": "Sam",
        "publish_date": "2000-07-16"
    },
    {
        "id": 4,
        "title": "The Flourist",
        "author": "Anna",
        "publish_date": "2004-08-05"
    }
]

app = FastAPI()

# list the books
@app.get("/book")
def get_book():
    return books

# get book by id
@app.get("/book/{book_id}")
def get_book_by_id(book_id: int):
    for book in books:
        if book.get("id") == book_id:  # or book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")

# add a book
class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/book")
def create_post(book: Book):
    new_book = book.model_dump()  # convert our pydantic model into dictionary.
    books.append(new_book)
    return {
        "message": "Book added successfully",
        "book": new_book
    }

# update a book
class BookUpdate(BaseModel):
    title: str
    author: str
    publish_date: str

@app.put("/book/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    for book in books:
        if book.get("id") == book_id:
            book.update(book_update.model_dump())
            return {
                "message": "Book updated successfully",
                "book": book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.get("id") == book_id:
            books.remove(book)
            return {
                "message": "Book deleted successfully"
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")