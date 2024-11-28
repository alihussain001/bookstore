from itertools import count

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from uuid import UUID
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    id:UUID
    title: str
    author: str
    description: Optional[str] = None
    rating: float

#In memory database (list)
BOOKS = []

# creating book data
@app.post("/books/")
def create_books(book: Book):
    BOOKS.append(book)
    return {"message": "Books added successfully", "book": book}

@app.get("/books/")
def get_books():
    return BOOKS
#
# @app.put("/{book_id}")
# def update_book(book_id: UUID, book: Books):
#     counter = 0
#
#     for x in book_id:
#         counter += 1
#         if x.id == book_id:
#             BOOKS[counter - 1] = book
#             return BOOKS[counter - 1]
#     raise HTTPException(status_code=404,detail= f"ID {book_id} : Does not exist")
#
# @app.delete("/{book_id}")
# def delete_book(book_id: UUID):
#     counter = 0
#
#     for x in BOOKS:
#         counter +=1
#         if x.id == book_id:
#             del BOOKS [counter - 1]
#             return f"ID: {book_id} deleted"
#     raise HTTPException(status_code=404, detail= f"ID {book_id} : Does not exist")

