# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tIuQjhz1ohemzST0EvaSG_wOI7L2u8Cx
"""

import os

class Book:
    def __init__(self, name, year, author, keyword):
        self.name = name
        self.year = year
        self.author = author
        self.keyword = keyword

    def __str__(self):
        return f"{self.name} {self.year} {self.author} {self.keyword}"

class Library:
    def __init__(self, id):
        self.id = id
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def edit_book(self, book, name, year, author, keyword):
        book.name = name
        book.year = year
        book.author = author
        book.keyword = keyword

    def print_books(self):
        for book in self.books:
            print(book)

def load_libraries():
    libraries = []
    for filename in os.listdir():
        if filename.endswith(".txt"):
            library_id = filename[:-4]
            library = Library(library_id)
            with open(filename, "r") as file:
                for line in file:
                    name, year, author, keyword = line.strip().split(" ")
                    book = Book(name, year, author, keyword)
                    library.add_book(book)
            libraries.append(library)
    return libraries

def save_libraries(libraries):
    for library in libraries:
        filename = f"{library.id}.txt"
        with open(filename, "w") as file:
            for book in library.books:
                file.write(str(book) + "\n")

def main():
    libraries = load_libraries()

    while True:
        print("1. Add a new library")
        print("2. Add a new book to a library")
        print("3. Delete a book from a library")
        print("4. Edit a book")
        print("5. Print library information")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library_id = input("Enter the library ID: ")
            library = Library(library_id)
            libraries.append(library)
            print("Library added successfully.")
        elif choice == "2":
            library_id = input("Enter the library ID: ")
            library = next((lib for lib in libraries if lib.id == library_id), None)
            if library:
                name = input("Enter the book name: ")
                year = input("Enter the publication year: ")
                author = input("Enter the author's name: ")
                keyword = input("Enter a keyword: ")
                book = Book(name, year, author, keyword)
                library.add_book(book)
                print("Book added successfully.")
            else:
                print("Library not found.")
        elif choice == "3":
            library_id = input("Enter the library ID: ")
            library = next((lib for lib in libraries if lib.id == library_id), None)
            if library:
                book_name = input("Enter the book name: ")
                book = next((b for b in library.books if b.name == book_name), None)
                if book:
                    library.remove_book(book)
                    print("Book deleted successfully.")
                else:
                    print("Book not found.")
            else:
                print("Library not found.")
        elif choice == "4":
            library_id = input("Enter the library ID: ")
            library = next((lib for lib in libraries if lib.id == library_id), None)
            if library:
                book_name = input("Enter the book name: ")
                book = next((b for b in library.books if b.name == book_name), None)
                if book:
                    name = input("Enter the new book name: ")
                    year = input("Enter the new publication year: ")
                    author = input("Enter the new author's name: ")
                    keyword = input("Enter a new keyword: ")
                    library.edit_book(book, name, year, author, keyword)
                    print("Book edited successfully.")
                else:
                    print("Book not found.")
            else:
                print("Library not found.")
        elif choice == "5":
            library_id = input("Enter the library ID: ")
            library = next((lib for lib in libraries if lib.id == library_id), None)
            if library:
                print(f"Library ID: {library.id}")
                print("Books:")
                library.print_books()
            else:
                print("Library not found.")
        elif choice == "6":
            save_libraries(libraries)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

